# Pruebas Unitarias del Proyecto Jekyll/Reveal.js

Este documento describe las pruebas unitarias implementadas para el proyecto de presentaciones Jekyll/Reveal.js.

## Estructura de Pruebas

Las pruebas están organizadas en la carpeta `tests/` y cubren los siguientes componentes:

### 1. **test_project.py** - Suite principal de pruebas

Incluye las siguientes clases de prueba:

#### `TestConfig`
Pruebas para el archivo de configuración `_config.yml`:
- ✅ Verifica que el archivo exista
- ✅ Valida campos requeridos (title, description, markdown, highlighter)
- ✅ Confirma que markdown esté configurado como `kramdown`
- ✅ Confirma que highlighter esté configurado como `rouge`
- ✅ Verifica que el plugin `jemoji` esté incluido

#### `TestLayouts`
Pruebas para los archivos de layout en `_layouts/`:
- ✅ Verifica existencia del directorio
- ✅ Confirma existencia de `presentation.html`, `slide.html`, y `print.html`
- ✅ Valida estructura HTML requerida en cada layout
- ✅ Verifica inclusión de partials (head.html, script.html)

#### `TestIncludes`
Pruebas para los archivos include en `_includes/`:
- ✅ Verifica existencia del directorio
- ✅ Confirma existencia de `head.html`, `script.html`, y `slide.html`
- ✅ Valida meta tags en head.html (charset, viewport, title)
- ✅ Verifica enlaces a CSS de reveal.js
- ✅ Confirma inicialización de Reveal en script.html

#### `TestPosts`
Pruebas para el directorio de posts `_posts/`:
- ✅ Verifica existencia del directorio
- ✅ Confirma que haya al menos un post
- ✅ Valida existencia del post introductorio
- ✅ Verifica formato correcto del front matter
- ✅ Confirma uso del layout `slide`

#### `TestScripts`
Pruebas para los scripts en `script/`:
- ✅ Verifica existencia del directorio
- ✅ Confirma existencia de `setup`, `server`, y `cibuild`
- ✅ Valida permisos de ejecución
- ✅ Verifica contenido correcto (jekyll serve, jekyll build, htmlproofer)

#### `TestRootFiles`
Pruebas para archivos en el directorio raíz:
- ✅ Verifica existencia de `_config.yml`, `Gemfile`, `index.html`
- ✅ Confirma existencia de `README.md` y `LICENSE`
- ✅ Valida que index.html use layout `presentation`
- ✅ Verifica loop through posts e inclusión de slide.html

## Ejecución de Pruebas

### Requisitos previos

```bash
pip install pyyaml
```

### Comandos de ejecución

Desde el directorio raíz del proyecto:

```bash
# Ejecutar todas las pruebas
python tests/run_tests.py

# Ejecutar en modo verbose
python tests/run_tests.py -v

# Ejecutar directamente con unittest
cd tests && python -m unittest test_project -v
```

## Resultados Esperados

Todas las pruebas deben pasar exitosamente:

```
----------------------------------------------------------------------
Ran 47 tests in 0.XXXs

OK
```

## Cobertura de Pruebas

| Componente | Archivos | Pruebas | Estado |
|------------|----------|---------|--------|
| Configuración | _config.yml | 5 | ✅ |
| Layouts | _layouts/*.html | 8 | ✅ |
| Includes | _includes/*.html | 11 | ✅ |
| Posts | _posts/*.md | 6 | ✅ |
| Scripts | script/* | 11 | ✅ |
| Archivos Raíz | Varios | 9 | ✅ |
| **Total** | **Todos** | **47** | **✅** |

## Mejoras Implementadas

Basado en los resultados de las pruebas, se verificó que:

1. ✅ Todos los archivos requeridos existen
2. ✅ La configuración es correcta para Jekyll + Reveal.js
3. ✅ Los layouts tienen la estructura HTML apropiada
4. ✅ Los includes contienen los elementos necesarios
5. ✅ Los posts siguen el formato correcto de Jekyll
6. ✅ Los scripts son ejecutables y tienen el contenido esperado

## Integración Continua

El script `script/cibuild` incluye validación automática:

```bash
#!/bin/sh
set -e
bundle exec jekyll build --baseurl "."
htmlproofer _site/index.html --empty-alt-ignore
```

Esto asegura que:
- El sitio se construye correctamente
- Los enlaces HTML son válidos
- No hay problemas de accesibilidad básicos

## Mantenimiento

Para agregar nuevas pruebas:

1. Crear nuevos métodos en las clases existentes
2. O crear nuevas clases siguiendo el patrón establecido
3. Asegurar que todas las pruebas pasen antes de hacer commit
4. Actualizar este README si se agregan nuevas categorías de pruebas
