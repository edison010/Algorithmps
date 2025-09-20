# Actividad: Algoritmo simple para romper contraseñas (fuerza bruta controlada)

## Objetivo
Implementar un algoritmo secuencial de fuerza bruta que genere combinaciones posibles y pruebe hasta encontrar una contraseña objetivo.

## Archivos
- `bruteforce.py` — script principal que genera combinaciones secuenciales y busca la contraseña.
- `README.md` — instrucciones y explicación.
- `.gitignore` — archivos y carpetas a ignorar (recomendado).

## Requisitos
- Python 3.8 o superior
- Git (para clonar/subir cambios)

## Cómo ejecutar

1. Clona el repositorio (si aún no lo tienes):
```bash
git clone https://github.com/edison010/Algorithmps.git
cd Algorithmps
```

2. Ejecuta el script:
```bash
python bruteforce.py
```

3. Cuando se solicite:
```
Ingrese la contrasela a decifrar:
```
escribe la contraseña de prueba (por ejemplo `a`, `ab`, `A1`).

## Descripción del algoritmo
- Alfabeto por defecto: `string.ascii_letters + string.digits` (letras mayúsculas, minúsculas y dígitos).
- El script prueba combinaciones de longitud 1 hasta 6 (`for longitud in range(1, 7)`).
- Para cada longitud imprime `Probando longitud N` y prueba todas las combinaciones secuenciales.
- Al encontrar la contraseña, imprime:
  - La contraseña encontrada.
  - Número de intentos realizados.
  - Tiempo de ejecución en segundos.

## Ejemplos de salida

**Ejemplo 1 — contraseña `a`**
```
Empezando a decifrar...
Probando longitud  1
Contraseña decifrada: a
Número de intentos: 1
Tiempo de ejecución: 0.0001 s
```

**Ejemplo 2 — contraseña `0a`** (salida parcial)
```
Empezando a decifrar...
Probando longitud  1
Probando longitud  2
...
0a
Contraseña decifrada: 0a
Número de intentos: 103
Tiempo de ejecución: 0.0023 s
```

> Nota: los tiempos y conteos dependen de la longitud del objetivo y el rendimiento del equipo.

## Reflexión / Análisis de seguridad
- El espacio de búsqueda crece exponencialmente con la longitud y el tamaño del alfabeto.  
- Para contraseñas largas (8+ caracteres) y alfabeto completo (mayúsculas, minúsculas, dígitos y símbolos), la fuerza bruta se vuelve impracticable sin hardware especializado.
- Buenas prácticas:
  - Usar contraseñas largas, usar simbolos especiales
  - Activar MFA (autenticación multifactor).
  - Implementar límites de intentos y hashing seguro (bcrypt, Argon2) en servidores.


## .gitignore sugerido
```
__pycache__/
*.pyc
.env
*.log
```