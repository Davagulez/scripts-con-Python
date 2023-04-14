import whisper
import glob

## Crear el archivo que guarda la info.
file = open('transcripcion.doc', 'x')#
file.close()


## Obtener y guardar los nombres de los archivos de audio
list = glob.glob("*.ogg")
list.sort()
print(list)


## transcribir y guardar en el archivo
model = whisper.load_model("small")
file = open('transcripcion.doc', 'w')
for l in list:
    result = model.transcribe(l)
    file.write("\n" + result['text'] + ". \n")
file.close()
print('Transcripción Finalizada')

