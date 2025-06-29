from pydantic import BaseModel, Field, validator


class Features(BaseModel):
    surface_reelle_bati: float = Field(..., gt=0, example=75.0)
    surface_terrain: float | None = Field(None, ge=0, example=50.0)
    nombre_lots: int = Field(..., ge=0, example=2)


class PredictionRequest(BaseModel):
    # on limite volontairement la ville à LILLE pour l’instant
    ville: str = Field(
        ...,
        pattern="LILLE",
        description="Ville supportée (actuellement seulement LILLE).",
        examples=["LILLE"],
    )
    type_local: str = Field(
        ...,
        pattern="APPARTEMENT|MAISON",
        description="Type de bien : APPARTEMENT ou MAISON.",
        examples=["APPARTEMENT"],
    )
    features: Features

    # ────────────────────────────────────────────────
    # Validators pour forcer la majuscule avant check
    # ────────────────────────────────────────────────
    @validator("ville", "type_local", pre=True)
    def to_upper(cls, v: str) -> str:
        return v.upper().strip()


class PredictionResponse(BaseModel):
    prix_m2_estime: float = Field(..., gt=0, example=3200.50)
