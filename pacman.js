function init() {
  // Créer un canvas
  var canvas = document.getElementById("canvas");
  var ctx = canvas.getContext("2d");

  // Créer un labyrinthe
  var labyrinthe = new Labyrinthe(ctx);

  // Créer un pacman
  var pacman = new Pacman(ctx, labyrinthe);

  // Créer des fantômes
  var fantomes = [];
  for (var i = 0; i < 5; i++) {
    var fantome = new Fantome(ctx, labyrinthe);
    fantomes.push(fantome);
  }

  // Démarrer le jeu
  startGame();
}

function startGame() {
  // Démarrer la boucle de jeu
  var loop = setInterval(update, 1000 / 60);

  // Gérer les événements clavier
  document.addEventListener("keydown", function(event) {
    switch (event.keyCode) {
      case 37: // Gauche
        pacman.moveLeft();
        break;
      case 38: // Haut
        pacman.moveUp();
        break;
      case 39: // Droite
        pacman.moveRight();
        break;
      case 40: // Bas
        pacman.moveDown();
        break;
    }
  });
}

function update() {
  // Mettre à jour le pacman
  pacman.update();

  // Mettre à jour les fantômes
  for (var i = 0; i < fantomes.length; i++) {
    fantomes[i].update();
  }

  // Vérifier les collisions
  for (var i = 0; i < fantomes.length; i++) {
    if (pacman.collidesWith(fantomes[i])) {
      // Le pacman a été touché par un fantôme
      gameOver();
    }
  }

  // Dessiner le labyrinthe
  labyrinthe.draw();

  // Dessiner le pacman
  pacman.draw();

  // Dessiner les fantômes
  for (var i = 0; i < fantomes.length; i++) {
    fantomes[i].draw();
  }
}

function gameOver() {
  // Arrêter la boucle de jeu
  clearInterval(loop);

  // Afficher un message de game over
  alert("Game over !");
}
