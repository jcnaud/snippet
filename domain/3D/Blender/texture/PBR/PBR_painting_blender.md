# PBR Painting Blender


## Tutorial
- Blender 2.8 Tutorial : PBR Texture Painting - https://www.youtube.com/watch?v=svzKoq3vew0

### Painting base / albedo
- Main tab: "Layout"
  - Window: "3D viewpoint"
    - [select object] Go to "Edit Mode"
      - Select the one face, future unwarp will use this face at start
      - Select all with "A"
      - uwrap with "u" -> "Folow Actives quads" -> Ok
    - [select object] + right click (menu:"Object context menu) -> "Shade Smooth"

- Main tab: "UV Editing"
  - Window: "UV Editor"
    - Make select move and scale on the UV to optimise the image surface

- Main tab: "Texture Paint"
  - Window: "Image Editor"
    - tab vselect: "Paint"

  - Window: "Properties"
    - tab: "Active Tool and Workspace settings"
      - Section: "Texture Slots"
        - "+" : add texture -> "Base Color"
          - Name: Base
          - Width: 2048 px 
          - Height: 2048 px
          Color: Blue
          - (button)"Ok"

  - Window: "3D Viewport"
    - tab: Texture Paint
      - tab: Viewport Shading: Material Preview
      - tab drop box: "Viewport Shading" -> "Scene Lights" enable

  - Main tab: "Texture Paint"
    - Window: "Image Editor"
      - tab: Vselect image : -> "Base"
      - tab: "Image*" -> "Save As" -> "Base.png"
  
### Painting bump
- Main tab: "Texture Paint"
  - Window: "Properties"
    - tab: "Active Tool and Workspace settings"
      - Section: "Texture Slots"
        - "+" : add texture -> "Bump"
          - Name: Bump
          - Width: 2048 px 
          - Height: 2048 px
          Color: Gray
          - (button)"Ok"
        - Select "Bump" material

  - Window: "3D Viewport"
    - tab: Texture Paint
      - Paint with black color to encrave
      - Paint with white color to extrude
      - "f" to reduce size paint

### Painting roughness
- Main tab: "Texture Paint"
  - Window: "Properties"
    - tab: "Active Tool and Workspace settings"
      - Section: "Texture Slots"
        - "+" : add texture -> "Roughness"
          - Name: Bump
          - Width: 2048 px 
          - Height: 2048 px
          Color: Gray
          - (button)"Ok"
        - Select "Roughness" material

  - Window: "3D Viewport"
    - tab: Texture Paint
      - Paint with black color to shiny
      - Paint with white color to rough
      - "f" to reduce size paint
      
### Check Shading
- Main tab: "Shading"
  - Window: "Shader Editor"
    - You can see shading construction

    