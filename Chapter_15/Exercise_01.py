class Date:
    def __init__(self, year: int, month: int, day: int):
        # Normalizamos días asumiendo meses fijos de 30 días
        extra_months, self.day = divmod(day - 1, 30)
        self.day += 1  # Base 1

        # Normalizamos meses
        total_months = (month - 1) + extra_months
        extra_years, self.month = divmod(total_months, 12)
        self.month += 1  # Base 1

        self.year = year + extra_years

    def __str__(self) -> str:
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    def is_after(self, other):
        if self.year > other.year:
            return True
        if self.year < other.year:
            return False

        if self.month > other.month:
            return True
        if self.month < other.month:
            return False

        return self.day > other.day

fecha1 = Date(2026, 9, 12)
fecha2 = Date(2025, 1, 1)

print(fecha1.is_after(fecha2))