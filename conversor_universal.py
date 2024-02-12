import streamlit as st

# Funciones de conversión
def temperatura():

    """Dependiendo el tipo de conversión imprimirá el resultado

    Dependiendo a qué quiere hacer la conversión el usuario se mostrará
    el número

    """
  
    st.subheader("Conversión de Temperatura")
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ("Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius")
    )
    if conversion == "Celsius a Fahrenheit":
        celsius = st.number_input("Ingresa la temperatura en Celsius")
        fahrenheit = celsius * 9/5 + 32
        st.write(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
    elif conversion == "Fahrenheit a Celsius":
        fahrenheit = st.number_input("Ingresa la temperatura en Fahrenheit")
        celsius = (fahrenheit - 32) * 5/9
        st.write(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius.")
    elif conversion == "Celsius a Kelvin":
        celsius = st.number_input("Ingresa la temperatura en Celsius")
        kelvin = celsius + 273.15
        st.write(f"{celsius} grados Celsius son {kelvin} grados Kelvin.")
    elif conversion == "Kelvin a Celsius":
        kelvin = st.number_input("Ingresa la temperatura en Kelvin")
        celsius = kelvin - 273.15
        st.write(f"{kelvin} grados Kelvin son {celsius} grados Celsius.")

def longitud():
    st.subheader("Conversión de Longitud")
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ("Pies a Metros", "Metros a Pies", "Pulgadas a Centímetros", "Centímetros a Pulgadas")
    )
    if conversion == "Pies a Metros":
        pies = st.number_input("Ingresa la longitud en Pies")
        metros = pies * 0.3048
        st.write(f"{pies} pies son {metros} metros.")
    elif conversion == "Metros a Pies":
        metros = st.number_input("Ingresa la longitud en Metros")
        pies = metros / 0.3048
        st.write(f"{metros} metros son {pies} pies.")
    elif conversion == "Pulgadas a Centímetros":
        pulgadas = st.number_input("Ingresa la longitud en Pulgadas")
        centimetros = pulgadas * 2.54
        st.write(f"{pulgadas} pulgadas son {centimetros} centímetros.")
    elif conversion == "Centímetros a Pulgadas":
        centimetros = st.number_input("Ingresa la longitud en Centímetros")
        pulgadas = centimetros / 2.54
        st.write(f"{centimetros} centímetros son {pulgadas} pulgadas.")

def peso_masa():
    st.subheader("Conversión de Peso/Masa")
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ("Libras a Kilogramos", "Kilogramos a Libras", "Onzas a Gramos", "Gramos a Onzas")
    )
    if conversion == "Libras a Kilogramos":
        libras = st.number_input("Ingresa el peso en Libras")
        kilogramos = libras * 0.453592
        st.write(f"{libras} libras son {kilogramos} kilogramos.")
    elif conversion == "Kilogramos a Libras":
        kilogramos = st.number_input("Ingresa el peso en Kilogramos")
        libras = kilogramos / 0.453592
        st.write(f"{kilogramos} kilogramos son {libras} libras.")
    elif conversion == "Onzas a Gramos":
        onzas = st.number_input("Ingresa el peso en Onzas")
        gramos = onzas * 28.3495
        st.write(f"{onzas} onzas son {gramos} gramos.")
    elif conversion == "Gramos a Onzas":
        gramos = st.number_input("Ingresa el peso en Gramos")
        onzas = gramos / 28.3495
        st.write(f"{gramos} gramos son {onzas} onzas.")

def volumen():
    st.subheader("Conversión de Volumen")
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ("Galones a Litros", "Litros a Galones", "Pulgadas cúbicas a Centímetros cúbicos", "Centímetros cúbicos a Pulgadas cúbicas")
    )
    if conversion == "Galones a Litros":
        galones = st.number_input("Ingresa el volumen en Galones")
        litros = galones * 3.78541
        st.write(f"{galones} galones son {litros} litros.")
    elif conversion == "Litros a Galones":
        litros = st.number_input("Ingresa el volumen en Litros")
        galones = litros / 3.78541
        st.write(f"{litros} litros son {galones} galones.")
    elif conversion == "Pulgadas cúbicas a Centímetros cúbicos":
        pulgadas_cubicas = st.number_input("Ingresa el volumen en Pulgadas cúbicas")
        centimetros_cubicos = pulgadas_cubicas * 16.3871
        st.write(f"{pulgadas_cubicas} pulgadas cúbicas son {centimetros_cubicos} centímetros cúbicos.")
    elif conversion == "Centímetros cúbicos a Pulgadas cúbicas":
        centimetros_cubicos = st.number_input("Ingresa el volumen en Centímetros cúbicos")
        pulgadas_cubicas = centimetros_cubicos / 16.3871
        st.write(f"{centimetros_cubicos} centímetros cúbicos son {pulgadas_cubicas} pulgadas cúbicas.")

def tiempo():
    st.subheader("Conversión de Tiempo")
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ("Horas a Minutos", "Minutos a Segundos", "Días a Horas", "Semanas a Días")
    )
    if conversion == "Horas a Minutos":
        horas = st.number_input("Ingresa el tiempo en Horas")
        minutos = horas * 60
        st.write(f"{horas} horas son {minutos} minutos.")
    elif conversion == "Minutos a Segundos":
        minutos = st.number_input("Ingresa el tiempo en Minutos")
        segundos = minutos * 60
        st.write(f"{minutos} minutos son {segundos} segundos.")
    elif conversion == "Días a Horas":
        dias = st.number_input("Ingresa el tiempo en Días")
        horas = dias * 24
        st.write(f"{dias} días son {horas} horas.")
    elif conversion == "Semanas a Días":
        semanas = st.number_input("Ingresa el tiempo en Semanas")
        dias = semanas * 7
        st.write(f"{semanas} semanas son {dias} días.")

def velocidad():
    st.subheader("Conversión de Velocidad")
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ("Millas por hora a Kilómetros por hora", "Kilómetros por hora a Metros por segundo", "Nudos a Millas por hora", "Metros por segundo a Pies por segundo")
    )
    if conversion == "Millas por hora a Kilómetros por hora":
        mph = st.number_input("Ingresa la velocidad en Millas por hora")
        kph = mph * 1.60934
        st.write(f"{mph} millas por hora son {kph} kilómetros por hora.")
    elif conversion == "Kilómetros por hora a Metros por segundo":
        kph = st.number_input("Ingresa la velocidad en Kilómetros por hora")
        mps = kph / 3.6
        st.write(f"{kph} kilómetros por hora son {mps} metros por segundo.")
    elif conversion == "Nudos a Millas por hora":
        nudos = st.number_input("Ingresa la velocidad en Nudos")
        mph = nudos * 1.15078
        st.write(f"{nudos} nudos son {mph} millas por hora.")
    elif conversion == "Metros por segundo a Pies por segundo":
        mps = st.number_input("Ingresa la velocidad en Metros por segundo")
        fps = mps * 3.28084
        st.write(f"{mps} metros por segundo son {fps} pies por segundo.")

def area():
    st.subheader("Conversión de Área")
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ("Metros cuadrados a Pies cuadrados", "Pies cuadrados a Metros cuadrados", "Kilómetros cuadrados a Millas cuadradas", "Millas cuadradas a Kilómetros cuadrados")
    )
    if conversion == "Metros cuadrados a Pies cuadrados":
        metros_cuadrados = st.number_input("Ingresa el área en Metros cuadrados")
        pies_cuadrados = metros_cuadrados * 10.764
        st.write(f"{metros_cuadrados} metros cuadrados son {pies_cuadrados} pies cuadrados.")
    elif conversion == "Pies cuadrados a Metros cuadrados":
        pies_cuadrados = st.number_input("Ingresa el área en Pies cuadrados")
        metros_cuadrados = pies_cuadrados / 10.764
        st.write(f"{pies_cuadrados} pies cuadrados son {metros_cuadrados} metros cuadrados.")
    elif conversion == "Kilómetros cuadrados a Millas cuadradas":
        km_cuadrados = st.number_input("Ingresa el área en Kilómetros cuadrados")
        millas_cuadradas = km_cuadrados * 0.386102
        st.write(f"{km_cuadrados} kilómetros cuadrados son {millas_cuadradas} millas cuadradas.")
    elif conversion == "Millas cuadradas a Kilómetros cuadrados":
        millas_cuadradas = st.number_input("Ingresa el área en Millas cuadradas")
        km_cuadrados = millas_cuadradas / 0.386102
        st.write(f"{millas_cuadradas} millas cuadradas son {km_cuadrados} kilómetros cuadrados.")

def energia():
    st.subheader("Conversión de Energía")
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ("Julios a Calorías", "Calorías a Kilojulios", "Kilovatios-hora a Megajulios", "Megajulios a Kilovatios-hora")
    )
    if conversion == "Julios a Calorías":
        julios = st.number_input("Ingresa la energía en Julios")
        calorias = julios / 4.184
        st.write(f"{julios} julios son {calorias} calorías.")
    elif conversion == "Calorías a Kilojulios":
        calorias = st.number_input("Ingresa la energía en Calorías")
        kilojulios = calorias * 0.004184
        st.write(f"{calorias} calorías son {kilojulios} kilojulios.")
    elif conversion == "Kilovatios-hora a Megajulios":
        kilovatios_hora = st.number_input("Ingresa la energía en Kilovatios-hora")
        megajulios = kilovatios_hora * 3.6
        st.write(f"{kilovatios_hora} kilovatios-hora son {megajulios} megajulios.")
    elif conversion == "Megajulios a Kilovatios-hora":
        megajulios = st.number_input("Ingresa la energía en Megajulios")
        kilovatios_hora = megajulios / 3.6
        st.write(f"{megajulios} megajulios son {kilovatios_hora} kilovatios-hora.")

def presion():
    st.subheader("Conversión de Presión")
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ("Pascales a Atmósferas", "Atmósferas a Pascales", "Barras a Libras por pulgada cuadrada", "Libras por pulgada cuadrada a Bares")
    )
    if conversion == "Pascales a Atmósferas":
        pascales = st.number_input("Ingresa la presión en Pascales")
        atm = pascales / 101325
        st.write(f"{pascales} pascales son {atm} atmósferas.")
    elif conversion == "Atmósferas a Pascales":
        atm = st.number_input("Ingresa la presión en Atmósferas")
        pascales = atm * 101325
        st.write(f"{atm} atmósferas son {pascales} pascales.")
    elif conversion == "Barras a Libras por pulgada cuadrada":
        barras = st.number_input("Ingresa la presión en Barras")
        psi = barras * 14.5038
        st.write(f"{barras} barras son {psi} libras por pulgada cuadrada.")
    elif conversion == "Libras por pulgada cuadrada a Bares":
        psi = st.number_input("Ingresa la presión en Libras por pulgada cuadrada")
        barras = psi / 14.5038
        st.write(f"{psi} libras por pulgada cuadrada son {barras} bares.")

def tamano_datos():
    st.subheader("Conversión de Tamaño de Datos")
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ("Megabytes a Gigabytes", "Gigabytes a Terabytes", "Kilobytes a Megabytes", "Terabytes a Petabytes")
    )
    if conversion == "Megabytes a Gigabytes":
        megabytes = st.number_input("Ingresa el tamaño en Megabytes")
        gigabytes = megabytes / 1024
        st.write(f"{megabytes} megabytes son {gigabytes} gigabytes.")
    elif conversion == "Gigabytes a Terabytes":
        gigabytes = st.number_input("Ingresa el tamaño en Gigabytes")
        terabytes = gigabytes / 1024
        st.write(f"{gigabytes} gigabytes son {terabytes} terabytes.")
    elif conversion == "Kilobytes a Megabytes":
        kilobytes = st.number_input("Ingresa el tamaño en Kilobytes")
        megabytes = kilobytes / 1024
        st.write(f"{kilobytes} kilobytes son {megabytes} megabytes.")
    elif conversion == "Terabytes a Petabytes":
        terabytes = st.number_input("Ingresa el tamaño en Terabytes")
        petabytes = terabytes / 1024
        st.write(f"{terabytes} terabytes son {petabytes} petabytes.")


# Título de la app
st.title("Conversor Universal")

# Categorías de conversión
categoria = st.sidebar.selectbox(
    "Selecciona una categoría:",
    ("Temperatura", "Longitud", "Peso/Masa", "Volumen", "Tiempo", "Velocidad", "Área", "Energía", "Presión", "Tamaño de Datos")
)

# Funciones de conversión
if categoria == "Temperatura":
    temperatura()
elif categoria == "Longitud":
    longitud()
elif categoria == "Peso/Masa":
    peso_masa()
elif categoria == "Volumen":
    volumen()
elif categoria == "Tiempo":
    tiempo()
elif categoria == "Velocidad":
    velocidad()
elif categoria == "Área":
    area()
elif categoria == "Energía":
    energia()
elif categoria == "Presión":
    presion()
elif categoria == "Tamaño de Datos":
    tamano_datos()
