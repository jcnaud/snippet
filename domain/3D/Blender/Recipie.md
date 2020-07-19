

# Plugin : Bool Tool
- (Main menu) Edit -> Preference
  - Add-ons
    - search Object: Bool Tool
- view: 3D Viewport
  - Select mutiple object
    - Ctrl+'-' : Add boolean modifier for each object to the last one

# Recepies : Hard surface
- In tab **3D viewport**
  - shift+a 
    - add cylinder
  - clic+right
    - shade smooth
- In tab **Properties**
  - tab: Object Data Proterties
    - Normal -> enable Auto Smooth

- Add object for cuting
  - ctrl+(-): Add-ons (Object: Bool Tool) to make bolean modifier
- Add modifier Bevel
  - Width: 0.006
  - segments: 3
  - Harden Normals: Enable
  - Limit Method : Angle


# Recepies: Bake Normal map
- Create an similar objec tin low and high poly
- On **3D viewport**
  - On high poly
    - Editmod: U -> Smart UV Project
      - Ok
  - On low poly
    - Editmod: U -> Smart UV Project
      - Ok
- On **Properties** 
  - Material propreties
    - Add material: name for example high
- Main tab **Shading**
  - On **Shader Editor**
    - On high poly material
      - Add node**Image texture**
        - Add image name, for example, "Backing"
    - On high poly material
      - Add node**Image texture**
        - Use existing image "Backing"
  - On **Properties**
    - tab Render Properties
      - Select "cycles" render engine
      - Go to "Bake"
        - Bake type: Normal
        - Selected to Active : True
        - Ray distance: 1m

  - On **outliner**
    - Slect the "High object"
    - Shift+select the "low Object"(Now au have 2 object selected and we bake from High to Low)
  - On **Properties**
    - tab Render Properties
      - Go to "Bake"
        - Button "Bake"
