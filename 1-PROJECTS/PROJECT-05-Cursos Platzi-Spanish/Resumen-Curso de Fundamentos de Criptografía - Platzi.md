# Resumen: Curso de Fundamentos de Criptografía - Platzi

## 📚 Visión General

Un curso completo que cubre desde conceptos históricos de criptografía hasta técnicas modernas de seguridad digital, combinando teoría matemática con implementaciones prácticas en Node.js.

## 🔑 Temas Principales

### 1. **Fundamentos e Historia (Lecciones 1-3)**

- La criptografía protege información mediante **confidencialidad, integridad, autenticidad y no repudio**
- Caso histórico: María Estuardo fue desmantelada mediante criptoanálisis
- Diferencia crítica: **Criptografía = cifrado matemático seguro** vs **Esteganografía = ocultamiento sin garantías criptográficas**

### 2. **Criptografía Clásica (Lección 4)**

- **Cifrado César**: desplazamiento simple (vulnerable)
- **Cifrado Vigenère**: usa clave repetida (más seguro)
- Técnicas de **sustitución y transposición**

### 3. **Generación de Aleatoriedad (Lecciones 5-6)**

- **RNG (Generadores de números aleatorios)**: producen entropía verdadera
- **PRNG (Pseudoaleatorios)**: deterministas pero impredecibles
- En Node.js: `crypto.randomBytes()`, `crypto.randomInt()`, `crypto.randomUUID()`

### 4. **Seguridad Criptográfica (Lecciones 7-8)**

- **Principio de Kerckhoffs**: el sistema debe ser seguro aunque el atacante conozca el algoritmo
- Modelos de ataque: COA (solo ciphertext), KPA (plaintext conocido)
- **Seguridad criptográfica** (teórica) vs **seguridad computacional** (práctica): las llaves suficientemente grandes (128+ bits) hacen ataques computacionalmente inviables

### 5. **Cifrado Simétrico (Lecciones 9-11)**

- **Cifrados por bloques**: procesan datos en bloques fijos
    - Modo ECB: vulnerable (patrones visibles)
    - Modo CBC: seguro semánticamente (encadena bloques)
- **Cifrados por flujo**: para streaming de datos
- **AES (Advanced Encryption Standard)**: estándar actual de facto, 10-14 rondas según tamaño de clave

### 6. **Funciones Hash (Lecciones 12-13)**

- **Hash**: función irreversible que comprime datos a tamaño fijo
- Propiedades: **resistencia a colisiones** y **resistencia a preimágenes**
- **HMAC**: añade clave secreta para autenticación de mensajes
- Algoritmos: SHA-256, SHA-512, Blake2

### 7. **Fundamentos Matemáticos (Lección 14)**

- **Aritmética modular**: agrupa números en ciclos (reloj)
- **Grupos matemáticos**: conjuntos con operaciones que cumplen cerradura, asociatividad, identidad e inverso
- Base de criptografía asimétrica moderna

### 8. **Criptografía Asimétrica - Intercambio de Llaves (Lecciones 15-17)**

- **Diffie-Hellman**: primer protocolo de intercambio seguro de llaves
    - Alice y Bob acuerdan secreto común sin transmitirlo
    - Seguridad: basada en dificultad del **logaritmo discreto**
    - Implementación con grupos predefinidos (ej: modp14)

### 9. **RSA y Firmas Digitales (Lecciones 18-19)**

- **RSA**: cifrado asimétrico usando pares de llaves (pública/privada)
- **Firma digital**:
    1. Hash del mensaje
    2. Encriptar hash con clave privada
    3. Verificar con clave pública
- Garantiza autenticidad y no repudio
- Implementación práctica: generación de llaves, firmado y verificación

### 10. **Criptografía de Curvas Elípticas (Lecciones 20-21)**

- **ECC**: operaciones matemáticas en curvas en lugar de números naturales
- **ECDSA**: firma digital con curvas elípticas
- Curvas populares: P-256 K1, P-256 R1
- Aplicaciones reales: chips de seguridad Apple, AWS KMS, llaves corporativas

### 11. **Infraestructura de Clave Pública - PKI (Lección 22)**

- **Autoridad de Certificación (CA)**: emite certificados digitales
- **Autoridad Registradora (RA)**: registra identidades
- Usos: HTTPS/TLS, e-commerce, trámites gubernamentales
- Ejemplo: candado verde en navegadores, firmas en SAT (México)

### 12. **Temas Avanzados (Lecciones 23-25)**

- **Sistemas interactivos de pruebas**: verificar cálculos complejos sin revelar datos
- **Computación cuántica**: amenaza teórica distante (requeriría ~1 millón de qubits; tecnología actual: ~1,000)
- **Resumen de primitivas**:
    - Sin clave: hashes, números aleatorios
    - Clave simétrica: AES, cifrados por flujo
    - Clave asimétrica: RSA, ECC, PKI

## ⚙️ Prácticas Implementadas

- Generación de números pseudoaleatorios
- Cifrado/descifrado con AES
- Cálculo de hashes y HMAC
- Intercambio Diffie-Hellman
- Generación y verificación de firmas RSA
- Implementación en Node.js con librería `crypto`

## 🎯 Conclusión

El curso proporciona un dominio integral de criptografía: desde principios matemáticos hasta aplicaciones modernas, con énfasis en implementación práctica segura.