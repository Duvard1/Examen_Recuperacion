import streamlit as st
import requests

# Inicializar el historial en session_state si no existe
if 'historial' not in st.session_state:
    st.session_state['historial'] = []

st.title("Clasificador de Texto y Transformador Binario")
st.text("Ingresa un texto y un número para obtener el conteo de vocales y su representación binaria")

# Entrada para el texto con validación
texto = st.text_area("Ingresa el texto:")

# Entrada para el número con validación
numero = st.text_input("Ingresa un número para convertir a binario:")

# Botón para procesar
if st.button("Procesar"):
    if texto and numero:
        # Enviar datos al backend
        respuesta = requests.post('http://localhost:9208/procesar', json={'texto': texto, 'numero': numero})

        if respuesta.status_code == 200:
            resultados = respuesta.json()
            st.subheader("Resultados")
            st.write(f"Numero Binario de {resultados['numero']}: {resultados['binario']}")
            st.write(f"Existen: {resultados['conteo_vocales']} vocales.")

            # Guardar en el historial
            st.session_state['historial'].append(resultados)
        else:
            st.warning(respuesta.json().get('error', 'Error desconocido'))
    else:
        st.warning("Por favor, ingresa un texto y un número")

# Mostrar historial de resultados
if st.session_state['historial']:
    st.subheader("Historial de Procesos")
    for idx, resultado in enumerate(st.session_state['historial'], 1):
        st.write(f"Resultado {idx}:")
        st.write(f"Cantidad de vocales: {resultado['conteo_vocales']}")
        st.write(f"Número: {resultado['numero']}, Binario: {resultado['binario']}")

#streamlit run main.py --server.port 8008
