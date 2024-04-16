import os
import json

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            trained_words = ", ".join(data.get('trainedWords', []))
            model_name = data.get('files', [{}])[0].get('name', '').replace('.safetensors', '')

            formatted_line = f"<lora:{model_name}:0.7>, {trained_words}\n"

            return formatted_line
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error al procesar el archivo {file_path}: {e}")
        return ''

def main():
    folder_path = input("Ingrese la ruta de la carpeta: ").strip()

    if not os.path.isdir(folder_path):
        print("La ruta ingresada no es válida o no es una carpeta.")
        return

    output_file_name = os.path.basename(folder_path) + '_resultados.txt'
    output_file_path = os.path.join(folder_path, output_file_name)

    with open(output_file_path, 'w') as output_file:
        for filename in os.listdir(folder_path):
            if filename.endswith('.civitai.info'):
                file_path = os.path.join(folder_path, filename)
                formatted_line = process_file(file_path)
                if formatted_line:
                    output_file.write(formatted_line)
                else:
                    print(f"No se pudo procesar el archivo {filename}")

    print(f"Proceso completado. Se ha generado el archivo de salida '{output_file_name}' en la misma carpeta.")

if __name__ == "__main__":
    main()
