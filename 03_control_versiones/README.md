**<h1 align="center">Comandos básicos de GIT</h1>**   
  
### gif config
Configuraciones generales de Git para nombre de usuario y correo electrónico.

```bash
git config --global user.name "nombre de usuario"
git config --global user.email "usuario@correo.com"
```

### git clone
Permite clonar un repositorio remoto.
```bash
git clone "URL del proyecto"
```

### git status
Mostrar el estado actual del repositorio, indicando el estado de los archivos de la rama de trabajo.
```bash
git status
```

### git add
Agregar cambios al directorio de trabajo (staging area), agrupa los cambios antes de ser confirmados en el repositorio.
```bash
git add .                #Agregar todos los cambios
git add "nombre arhivo"  #Agregar un archivo específico 
git add directorio/      #Agregar un directorio de trabajo
```

### git commit
Confirma los cambios (staging area) en el historial del repositorio.
```bash
git commit -m "mensaje descriptivo"
```

### git push
Envía los commit (cambios confirmados) del área local de la rama al repositorio remoto.
```bash
git push origin "nombre rama"
```

### git pull
Sirve para sincronizar el repositorio remoto con el repositorio local.
```bash
git pull origin "nombre rama"
```

### git branch
Se utiliza para gestionar las ramas de un repositorio de Git.
```bash
git branch #Listar todas las ramas locales del repositorio, la rama marcada con * es la rama actual
git branch "nombre rama" #Crear una nueva rama
```

### git switch
Permite cambiar a una rama específica.
```bash
git switch "nombre rama"
git switch -c "nombre rama" #Crea una rama nueva y cambia a ella automáticamente
```

### git merge
Permite combinar ramas, integrando los cambios de una rama en otra rama.
```bash
git merge "nombre rama" 
```
