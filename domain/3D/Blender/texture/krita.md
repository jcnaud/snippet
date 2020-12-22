# Krita texture


## Tutorial 
- Créer ses propres matériaux multitexture – TUTORIEL KRITA/BLENDER: https://www.youtube.com/watch?v=OgY72RtCKPA
- [HandPainted] Roof texture - https://www.youtube.com/watch?v=DX5376ehEKQ

## Methode

### On krita
- Create square image with size 2^x. e: 1024x1024
- Activate the mode seamless "Wraparound Tool" (W)
  - Settings -> Configure Krita -> search wrap (Add w key)
- Make texture with multiple layer and save it in .kra
- Diffuse
  - Save to *_diffuse in png.
- normal map
  - Merge layer
    - Filter -> edge detection -> height to normal map
  - Save to *_normal in png.
- roughness
  - Filter -> adjust -> Desaturate (image become gray)
  - Filter -> adjust -> Level
  - Save to *_roughness in png.
- displacement
  - Filter -> adjust -> Desaturate (image become gray)
  - Filter -> adjust -> Level
  - Save to *_displacement in png.
