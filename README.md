# 📌 Replicación Óptima de Archivos en Servidores

> ⚠️ Estado: ***EN DESARROLLO*** Versión académica

Implementacion de un algoritmo de **programación dinámica** para determinar la ubicación óptima de copias de un archivo en una red de servidores, minimizando el **costo total** de acceso y colocación. Basado en un problema de optimización típico de *Dynamic Programming*.

---

## 👥 Autores

* [JUAN SEBASTIÁN GUAYAZÁN CLAVIJO](https://github.com/JSGC-ECI) → [juan.guayazan-c@mail.escuelaing.edu.co](mailto:juan.guayazan-c@mail.escuelaing.edu.co)
Teoría de la Programación (ISIS TPRO-1)   
Decanatura Ingeniería de Sistemas → Centro de Estudios de Ingeniería de Software  
Ingeniería de Sistemas e Ingeniería Estadística  
Escuela Colombiana de Ingeniería Julio Garavito  
2024-2

---

## 🧠 Índice

* 📌 [Nombre del Proyecto](#-nombre-del-proyecto)
* 👥 [Autores](#-autores)
* 🚀 [Características](#-características)
* ⚙️ [Tecnologías](#️-tecnologías)
* 📦 [Instalación y Requisitos](#-instalación-y-requisitos)
* ▶️ [Uso](#️-uso)
* 🧪 [Pruebas](#-pruebas)
* 📁 [Estructura del Proyecto](#-estructura-del-proyecto)
* 📌 [TODOs / Funcionalidades Futuras](#-todos--funcionalidades-futuras)
* 📊 [Estadísticas del Repositorio](#-estadísticas-del-repositorio)
* 📄 [Licencia](#-licencia)

---

## 🚀 Características

* ✅ Algoritmo de programación dinámica para encontrar el costo mínimo total.
* ✅ Cálculo de costo de colocación y costo de acceso según la distancia entre servidores.
* ✅ Propósito académico para la comprensión de algoritmos de optimización.

---

## ⚙️ Tecnologías

* Lenguaje(s): `Haskell`, `Python`
* Herramientas: `GHCi`, `Python 3.x`
* Dependencias: `math` (Python)

---

## 📦 Instalación y Requisitos

### Clonar el repositorio

```bash
git clone https://github.com/JSGC-ECI/TPRO
```

### Requisitos

* Python 3.8+
* GHC o GHCi para Haskell
* Editor de código (VS Code recomendado)

### Instalación

1. Abrir el proyecto en tu IDE favorito.
2. Ejecutar el archivo `.py` o `.hs` según el lenguaje deseado.

---

## ▶️ Uso

Describe cómo se ejecuta el programa:

> \[!NOTE]
> Este código calcula el costo mínimo total y determina dónde colocar copias del archivo.

> \[!WARNING]
> El algoritmo asume que siempre hay una copia en el último servidor.

> \[!TIP]
> Puedes modificar la lista de costos de colocación para simular diferentes escenarios.

> \[!IMPORTANT]
> Asegúrate de usar valores positivos para los costos.

---

## 🧪 Pruebas

```bash
# Python
python3 main.py

# Haskell
ghci main.hs
```

```python
c = [4, 23, 43, 56, 75]
print(calcular_minimo_costo(c))
```

---

## 📁 Estructura del Proyecto

```bash
📦 minimizacion-costos-replicacion
 ┣ 📜 12.py          # Implementación en Python
 ┗ 📜 12.hs          # Implementación en Haskell
```

---

## 📌 TODOs / Funcionalidades Futuras

* [ ] Visualización gráfica de resultados
* [ ] Soporte para más métricas de costo
* [ ] Interfaz web interactiva

---

## 📊 Estadísticas del Repositorio

![Lenguaje principal](https://img.shields.io/github/languages/top/JSGC-ECI/TPRO?style=flat-square)
![Tamaño del repositorio](https://img.shields.io/github/repo-size/JSGC-ECI/TPRO?style=flat-square)
![Stars](https://img.shields.io/github/stars/JSGC-ECI/TPRO?style=flat-square)
![Forks](https://img.shields.io/github/forks/JSGC-ECI/TPRO?style=flat-square)
![Issues abiertas](https://img.shields.io/github/issues/JSGC-ECI/TPRO?style=flat-square)

---

## 📄 Licencia

Este proyecto está licenciado bajo propósitos académicos y educativos. Puedes consultar el archivo [LICENSE](./LICENSE) para más información.
