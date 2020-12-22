# Textures

## Links free
https://texturehaven.com/
pavement

## Type
Diffuse : alias texture
AO (aka Ambient Occlusion): only shadow of the diffuse
Albedo: like diffuse without shadow
Displacement: Geometry modification
Normal: Normal map (like bump or depth but in 3D)
Reflection (aka Specularity):  Where is the reflection and where not
Rougness (invert of Gloss):  control sharpess of refflection,  more Roughnees mean more white
Rough Ao


## Normal map

- Add like image
  - Color Space : Non-Color
- Add **Normal Map** node
  - Connect Previous node -> color to this node -> color
  - connect This node -> Normal to Principed BSDF -> Normal
  - Upgrade this node -> Strength to see the influence of normal 

## Rougness
- Add like image
  - Color Space : Non-Color
  - connect This node -> Color to Principed BSDF -> Roughness

Options:
 - Use ColorRamp