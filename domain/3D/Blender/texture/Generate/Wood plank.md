# Wood plank


## Tutorial
- Blender Wood Material... (oh, and it's procedural) - https://www.youtube.com/watch?v=EoQgq7n9Rwk


## Generate Woond plaque

- Main tab: "Layout"
  - Window: "3D viewpoint"
    - Delete All object
    - shift + a: Add "Messh"->"Plane"

  - Window: "Properties"
    - tab: "Render Properties"
      - "Render Engine": "Cycles"
      - "Device": "GPU Compute"
      - section: "Film"
        - "Transparent": Enable


- Main tab: "Shading"
  - Window: "Shader Editor"
    - "+New" materal name "woodenplanks"
    - Delete Node "Priniped BSDF"
    - tab: "Add" -> "Search" -> "Brick texture"