from datetime import datetime, timedelta

alimentos = []


alimentos.append(("leche", "2025-05-01"))
alimentos.append(("pan", "2025-04-29"))
alimentos.append(("yogurt", "2025-05-03"))

hoy = datetime.today()

print("\n🥕 Alimentos por caducar en 3 días:\n")
for nombre, fecha_str in alimentos:
    fecha_venc = datetime.strptime(fecha_str, "%Y-%m-%d")
    if 0 <= (fecha_venc - hoy).days <= 3:
        print(f"⚠️ {nombre} vence pronto el {fecha_venc.date()}")