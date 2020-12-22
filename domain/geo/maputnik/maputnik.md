# Maputnik

## Tutorial from scratch

Go to: https://maputnik.github.io/editor

- Delete all layers.

- Tab: Data Sources
  - Delete all data source
  - Add (clcik):  OpenMapTiles V3
  - Close the dialog
- View: inpect (Check you have data)
- View: Map (It will be black)
- Add Layer:
  - ID: bg
  - Type : Background
- Layer -> bg
  - Color: rgb(185,185,185)
- Add Layer:
  - ID: water
  - Type : Fill
  - Source : openmaptiles
  - Source Layer : water
- Layer -> water
  - Opacity: 0.7
  - Color: rgb(34, 109, 195)
- Add Layer:
  - ID: boundary
  - Type : line
  - Source : openmaptiles
  - Source Layer : boundary
- Layer -> boundary
  - Color: rgb(90, 90, 90)
