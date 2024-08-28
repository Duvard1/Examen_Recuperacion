from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/procesar', methods=['POST'])
def procesar():
    data = request.json
    texto = data.get('texto', '')
    numero = data.get('numero', '')

    # Validar que el texto no tenga números
    if any(char.isdigit() for char in texto):
        return jsonify({"error": "No puedo generar una respuesta, porque solo tengo el entrenamiento en binario y contar vocales."}), 400

    # Validar que el número sea un dígito
    if not numero.isdigit():
        return jsonify({"error": "No puedo generar una respuesta, porque solo tengo el entrenamiento en binario y contar vocales."}), 400

    # Convertir el número a entero
    numero_entero = int(numero)

    # Contar las vocales en el texto
    vocales = 'aeiouAEIOU'
    conteo_vocales = sum(1 for char in texto if char in vocales)

    # Convertir el número a binario
    binario = bin(numero_entero)[2:]

    # Responder con los resultados
    return jsonify({
        "conteo_vocales": conteo_vocales,
        "numero": numero_entero,
        "binario": binario
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9208)
