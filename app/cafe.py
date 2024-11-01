import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        expiration_date = visitor["vaccine"].get("expiration_date")
        if not isinstance(expiration_date, datetime.date):
            raise ValueError("Invalid expiration date format.")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        return f"Welcome to {self.name}"
