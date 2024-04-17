"""Si queremos hacer un juego de fútbol donde hay diferentes equipos con estilos de juego únicos,
uniformes distintivos y estadios específicos. Cada equipo tiene su propio conjunto de jugadores, entrenadores y aficionados,
así como tácticas de juego específicas. Entonces, podríamos utilizar el patrón Abstract Factory para crear una fábrica abstracta para cada equipo,
que proporcionaría métodos para crear diferentes tipos de elementos relacionados con ese equipo. 
Por ejemplo, tendríamos una interfaz TeamFactory con métodos como crearJugador(), crearEntrenador() y crearEstadio().
Luego, tendríamos implementaciones concretas de esta interfaz para cada equipo, como RealMadridFactory, BarcelonaFactory y LiverpoolFactory,
que proporcionarían las clases concretas de jugadores, entrenadores y estadios para cada equipo."""
