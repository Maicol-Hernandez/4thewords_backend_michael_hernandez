import os
from sqlmodel import Session
from app.models.legend import Legend
from fastapi import HTTPException


class LegendService:
    def __init__(self, session: Session):
        self.session = session

    def create_legend(self, legend_data: dict, image_url: str) -> Legend:
        legend = Legend(**legend_data, image_url=image_url)
        self.session.add(legend)
        self.session.commit()
        self.session.refresh(legend)
        return legend

    def get_legends(self, filters: dict):
        query = self.session.query(Legend)

        if filters.get("name") is not None:
            query = query.filter(Legend.name == filters["name"])
        if filters.get("created_at") is not None:
            query = query.filter(Legend.created_at == filters["created_at"])
        if filters.get("category") is not None:
            query = query.filter(Legend.category == filters["category"])
        if filters.get("province") is not None:
            query = query.filter(Legend.province == filters["province"])
        if filters.get("canton") is not None:
            query = query.filter(Legend.canton == filters["canton"])
        if filters.get("district") is not None:
            query = query.filter(Legend.district == filters["district"])

        return query.all()

    def update_legend(self, legend_id: int, legend_data: dict, image_url: str) -> Legend:
        legend = self.session.get(Legend, legend_id)
        if not legend:
            raise HTTPException(status_code=404, detail="Legend not found")

        old_image_url = legend.image_url
        legend.image_url = image_url

        for key, value in legend_data.items():
            setattr(legend, key, value)

        self.session.commit()
        self.session.refresh(legend)

        # Elimina la imagen antigua
        print("condicional", old_image_url and old_image_url != image_url)
        if old_image_url and old_image_url != image_url:
            self._delete_image(old_image_url)

        return legend

    def delete_legend(self, legend_id: int):
        legend = self.session.get(Legend, legend_id)
        if not legend:
            raise HTTPException(status_code=404, detail="Legend not found")

        self.session.delete(legend)
        self.session.commit()
        return True

    def _delete_image(self, image_url: str):
        """Elimina un archivo de imagen del sistema de archivos."""
        filename = os.path.basename(image_url)
        static_dir = os.path.abspath("app/static")
        file_path = os.path.join(static_dir, filename)

        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error al eliminar la imagen: {str(e)}"
            )
