<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flappy Bird Clone</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #70c5ce;
        }
        canvas {
            border: 2px solid #000;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="400" height="600"></canvas>
    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        let bird = { x: 50, y: 150, width: 34, height: 24, gravity: 0.6, lift: -15, velocity: 0 };
        let pipes = [];
        let frame = 0;
        let score = 0;
        let gameOver = false;

        function drawBird() {
            ctx.fillStyle = "yellow";
            ctx.fillRect(bird.x, bird.y, bird.width, bird.height);
        }

        function drawPipes() {
            ctx.fillStyle = "green";
            pipes.forEach(pipe => {
                ctx.fillRect(pipe.x, 0, pipe.width, pipe.height);
                ctx.fillRect(pipe.x, pipe.height + 150, pipe.width, canvas.height - pipe.height - 150);
            });
        }

        function updatePipes() {
            if (frame % 75 === 0) {
                let pipeHeight = Math.random() * (canvas.height - 150) + 50;
                pipes.push({ x: canvas.width, height: pipeHeight, width: 50 });
            }
            pipes.forEach(pipe => {
                pipe.x -= 2;
            });
            if (pipes.length > 0 && pipes[0].x < -pipes[0].width) {
                pipes.shift();
                score++;
            }
        }

        function checkCollision() {
            pipes.forEach(pipe => {
                if (bird.x + bird.width > pipe.x && bird.x < pipe.x + pipe.width) {
                    if (bird.y < pipe.height || bird.y + bird.height > pipe.height + 150) {
                        gameOver = true;
                    }
                }
            });
            if (bird.y + bird.height >= canvas.height || bird.y < 0) {
                gameOver = true;
            }
        }

        function resetGame() {
            bird.y = 150;
            bird.velocity = 0;
            pipes = [];
            score = 0;
            frame = 0;
            gameOver = false;
        }

        function gameLoop() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            if (!gameOver) {
                bird.velocity += bird.gravity;
                bird.y += bird.velocity;

                drawBird();
                updatePipes();
                drawPipes();
                checkCollision();

                ctx.fillStyle = "black";
                ctx.fillText("Score: " + score, 10, 20);
                frame++;
            } else {
                ctx.fillStyle = "black";
                ctx.fillText("Game Over! Score: " + score, 50, canvas.height / 2);
                ctx.fillText("Press R to Restart", 50, canvas.height / 2 + 20);
            }
            requestAnimationFrame(gameLoop);
        }

        document.addEventListener("keydown", (event) => {
            if (event.code === "Space" && !gameOver) {
                bird.velocity = bird.lift;
            }
            if (event.code === "KeyR" && gameOver) {
                resetGame();
            }
        });

        gameLoop();
    </script>
</body>
</html>
