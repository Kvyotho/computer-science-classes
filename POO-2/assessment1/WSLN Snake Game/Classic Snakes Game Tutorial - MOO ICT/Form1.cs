using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Drawing.Imaging; // add this for the JPG compressor

namespace Classic_Snakes_Game_Tutorial___MOO_ICT
{
    public partial class Form1 : Form
    {

        private List<Circle> Snake = new List<Circle>();
        private Circle food = new Circle();
        private Circle chaosFruit = new Circle();
        private Circle dangerFruit = new Circle();

        int maxWidth;
        int maxHeight;

        int score;
        int highScore;

        Random rand = new Random();

        bool goLeft, goRight, goDown, goUp;

        bool controlsInverted = false;
        int effectTimer = 0;

        int baseSpeed = 120;
        int speedBoostTimer = 0;

        int boostCharges = 0;
        bool boostActive = false;
        int boostTimer = 0;

        string currentEffect = "None";


        public Form1()
        {
            
            InitializeComponent();
            this.KeyPreview = true;
            new Settings();
        }

        private void KeyIsDown(object sender, KeyEventArgs e)
        {

            if (e.KeyCode == Keys.Left)
            {
                if (controlsInverted)
                {
                    if (Settings.directions != "left")
                        goRight = true;
                }
                else
                {
                    if (Settings.directions != "right")
                        goLeft = true;
                }
            }

            if (e.KeyCode == Keys.Right)
            {
                if (controlsInverted)
                {
                    if (Settings.directions != "right")
                        goLeft = true;
                }
                else
                {
                    if (Settings.directions != "left")
                        goRight = true;
                }
            }

            if (e.KeyCode == Keys.Up)
            {
                if (controlsInverted)
                {
                    if (Settings.directions != "up")
                        goDown = true;
                }
                else
                {
                    if (Settings.directions != "down")
                        goUp = true;
                }
            }

            if (e.KeyCode == Keys.Down)
            {
                if (controlsInverted)
                {
                    if (Settings.directions != "down")
                        goUp = true;
                }
                else
                {
                    if (Settings.directions != "up")
                        goDown = true;
                }
            }

            if (e.KeyCode == Keys.Space)
            {
                if (boostCharges > 0 && !boostActive && !(speedBoostTimer > 0))
                {
                    boostCharges--;
                    boostActive = true;
                    boostTimer = 40;

                    gameTimer.Interval = Math.Max(20, baseSpeed - 20);

                    lblBoost.Text = "Boosts: " + boostCharges;
                    lblEffect.Text = "Effect: SPEED BOOST";
                }
            }


        }

        private void KeyIsUp(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Left)
            {
                goLeft = false;
            }
            if (e.KeyCode == Keys.Right)
            {
                goRight = false;
            }
            if (e.KeyCode == Keys.Up)
            {
                goUp = false;
            }
            if (e.KeyCode == Keys.Down)
            {
                goDown = false;
            }
        }

        private void StartGame(object sender, EventArgs e)
        {
            RestartGame();
        }

        private void TakeSnapShot(object sender, EventArgs e)
        {
            Label caption = new Label();
            caption.Text = "I scored: " + score + " and my Highscore is " + highScore + " on the Snake Game from MOO ICT";
            caption.Font = new Font("Ariel", 12, FontStyle.Bold);
            caption.ForeColor = Color.Purple;
            caption.AutoSize = false;
            caption.Width = picCanvas.Width;
            caption.Height = 30;
            caption.TextAlign = ContentAlignment.MiddleCenter;
            picCanvas.Controls.Add(caption);

            SaveFileDialog dialog = new SaveFileDialog();
            dialog.FileName = "Snake Game SnapShot MOO ICT";
            dialog.DefaultExt = "jpg";
            dialog.Filter = "JPG Image File | *.jpg";
            dialog.ValidateNames = true;

            if (dialog.ShowDialog() == DialogResult.OK)
            {
                int width = Convert.ToInt32(picCanvas.Width);
                int height = Convert.ToInt32(picCanvas.Height);
                Bitmap bmp = new Bitmap(width, height);
                picCanvas.DrawToBitmap(bmp, new Rectangle(0,0, width, height));
                bmp.Save(dialog.FileName, ImageFormat.Jpeg);
                picCanvas.Controls.Remove(caption);
            }





        }

        private void ResetMovement()
        {
            goLeft = false;
            goRight = false;
            goUp = false;
            goDown = false;
        }
        private void GameTimerEvent(object sender, EventArgs e)
        {

            // boost timer
            if (boostActive)
            {
                boostTimer--;

                if (boostTimer <= 0)
                {
                    boostActive = false;
                    gameTimer.Interval = baseSpeed;

                    lblEffect.Text = "Effect: None";
                }
            }

            // handles temporary effects

            if (effectTimer > 0)
            {
                effectTimer--;

                if (effectTimer == 0)
                {
                    controlsInverted = false;
                    ResetMovement();
                    lblEffect.Text = "Effect: None";
                }
            }

            if (speedBoostTimer > 0)
            {
                speedBoostTimer--;

                if (speedBoostTimer == 0)
                {
                    gameTimer.Interval = baseSpeed;
                    lblEffect.Text = "Effect: None";
                }
            }

            // setting the directions

            if (goLeft)
            {
                Settings.directions = "left";
            }
            if (goRight)
            {
                Settings.directions = "right";
            }
            if (goDown)
            {
                Settings.directions = "down";
            }
            if (goUp)
            {
                Settings.directions = "up";
            }
            // end of directions

            for (int i = Snake.Count - 1; i >= 0; i--)
            {
                if (i == 0)
                {

                    switch (Settings.directions)
                    {
                        case "left":
                            Snake[i].X--;
                            break;
                        case "right":
                            Snake[i].X++;
                            break;
                        case "down":
                            Snake[i].Y++;
                            break;
                        case "up":
                            Snake[i].Y--;
                            break;
                    }

                    if (Snake[i].X < 0)
                    {
                        Snake[i].X = maxWidth;
                    }
                    if (Snake[i].X > maxWidth)
                    {
                        Snake[i].X = 0;
                    }
                    if (Snake[i].Y < 0)
                    {
                        Snake[i].Y = maxHeight;
                    }
                    if (Snake[i].Y > maxHeight)
                    {
                        Snake[i].Y = 0;
                    }


                    if (Snake[i].X == food.X && Snake[i].Y == food.Y)
                    {
                        EatFood();
                    }

                    // chaos fruit collision
                    if (Snake[i].X == chaosFruit.X && Snake[i].Y == chaosFruit.Y)
                    {
                        ActivateRandomEffect();

                        chaosFruit = new Circle
                        {
                            X = rand.Next(2, maxWidth),
                            Y = rand.Next(2, maxHeight)
                        };
                    }

                    // danger fruit collision
                    if (Snake[i].X == dangerFruit.X && Snake[i].Y == dangerFruit.Y)
                    {
                        score = Math.Max(0, score - 5);
                        txtScore.Text = "Score: " + score;

                        if (Snake.Count > 3)
                        {
                            Snake.RemoveRange(Snake.Count - 2, 2);
                        }

                        lblEffect.Text = "Poison! -5 Score.";

                        dangerFruit = new Circle
                        {
                            X = rand.Next(2, maxWidth),
                            Y = rand.Next(2, maxHeight)
                        };
                    }

                    for (int j = 1; j < Snake.Count; j++)
                    {

                        if (Snake[i].X == Snake[j].X && Snake[i].Y == Snake[j].Y)
                        {
                            GameOver();
                        }

                    }


                }
                else
                {
                    Snake[i].X = Snake[i - 1].X;
                    Snake[i].Y = Snake[i - 1].Y;
                }
            }


            picCanvas.Invalidate();

        }

        private void UpdatePictureBoxGraphics(object sender, PaintEventArgs e)
        {
            Graphics canvas = e.Graphics;

            Brush snakeColour;

            for (int i = 0; i < Snake.Count; i++)
            {
                if (i == 0)
                {
                    snakeColour = Brushes.Black;
                }
                else
                {
                    snakeColour = Brushes.DarkGreen;
                }

                canvas.FillEllipse(snakeColour, new Rectangle
                    (
                    Snake[i].X * Settings.Width,
                    Snake[i].Y * Settings.Height,
                    Settings.Width, Settings.Height
                    ));
            }


            canvas.FillEllipse(Brushes.DarkRed, new Rectangle
            (
            food.X * Settings.Width,
            food.Y * Settings.Height,
            Settings.Width, Settings.Height
            ));

            canvas.FillEllipse(Brushes.Purple, new Rectangle
            (
            dangerFruit.X * Settings.Width,
            dangerFruit.Y * Settings.Height,
            Settings.Width, Settings.Height
            ));

            Point[] triangle =
            {
                new Point(chaosFruit.X * Settings.Width + Settings.Width / 2, chaosFruit.Y * Settings.Height),
                new Point(chaosFruit.X * Settings.Width, chaosFruit.Y * Settings.Height + Settings.Height),
                new Point(chaosFruit.X * Settings.Width + Settings.Width, chaosFruit.Y * Settings.Height + Settings.Height)
            };

            canvas.FillPolygon(Brushes.Gold, triangle);
        }

        private void RestartGame()
        {

            maxWidth = picCanvas.Width / Settings.Width - 1;
            maxHeight = picCanvas.Height / Settings.Height - 1;

            Snake.Clear();

            controlsInverted = false;
            effectTimer = 0;
            speedBoostTimer = 0;
            boostCharges = 0;
            boostActive = false;
            boostTimer = 0;

            baseSpeed = 120;
            gameTimer.Interval = baseSpeed;

            startButton.Enabled = false;
            snapButton.Enabled = false;
            score = 0;
            txtScore.Text = "Score: " + score;
            lblBoost.Text = "Boosts: 0";
            lblEffect.Text = "Effect: None";

            Circle head = new Circle { X = 10, Y = 5 };
            Snake.Add(head); // adding the head part of the snake to the list

            for (int i = 0; i < 10; i++)
            {
                Circle body = new Circle();
                Snake.Add(body);
            }

            food = new Circle { X = rand.Next(2, maxWidth), Y = rand.Next(2, maxHeight)};
            chaosFruit = new Circle { X = rand.Next(2, maxWidth), Y = rand.Next(2, maxHeight) };
            dangerFruit = new Circle { X = rand.Next(2, maxWidth), Y = rand.Next(2, maxHeight) };

            gameTimer.Start();

        }

        private void EatFood()
        {
            score += 5;

            txtScore.Text = "Score: " + score;

            // speed increases every 5 points
            // if modifying score in anything other than +5 and -5, change this logic
            if (score % 5 == 0 && gameTimer.Interval > 30)
            {
                gameTimer.Interval -= 10;
                baseSpeed = gameTimer.Interval; //sets base speed to new speed
            }

            Circle body = new Circle
            {
                X = Snake[Snake.Count - 1].X,
                Y = Snake[Snake.Count - 1].Y
            };

            Snake.Add(body);

            food = new Circle { X = rand.Next(2, maxWidth), Y = rand.Next(2, maxHeight) };


        }

        private void ActivateRandomEffect()
        {
            int effect = rand.Next(0, 6);

            switch (effect)
            {
                case 0: // increase size +5
                    for (int i = 0; i < 5; i++)
                    {
                        Circle body = new Circle
                        {
                            X = Snake[Snake.Count - 1].X,
                            Y = Snake[Snake.Count - 1].Y
                        };
                        Snake.Add(body);
                    }
                    lblEffect.Text = "Effect: GROWTH";
                    break;

                case 1: // decrease size -5
                    if (Snake.Count > 6)
                    {
                        Snake.RemoveRange(Snake.Count - 5, 5);
                    }
                    lblEffect.Text = "Effect: SHRINK";
                    break;

                case 2: // temp speed boost
                    gameTimer.Interval = Math.Max(30, baseSpeed - 30);
                    speedBoostTimer = 50;
                    lblEffect.Text = "Effect: CHAOS SPEED";
                    break;

                case 3: // temp inverted controls
                    controlsInverted = true;
                    effectTimer = 80;
                    ResetMovement();
                    lblEffect.Text = "Effect: INVERTED CONTROLS";
                    break;

                case 4: // bonus score +5
                    score += 5;
                    txtScore.Text = "Score: " + score;
                    break;

                case 5: // boost charge
                    boostCharges += 2;
                    lblBoost.Text = "Boosts: " + boostCharges;

                    currentEffect = "BOOST FOUND";
                    lblEffect.Text = "Effect: Boost +2";
                    break;
            }
        }

        private void GameOver()
        {
            gameTimer.Stop();
            startButton.Enabled = true;
            snapButton.Enabled = true;

            if (score > highScore)
            {
                highScore = score;

                txtHighScore.Text = "High Score: " + Environment.NewLine + highScore;
                txtHighScore.ForeColor = Color.Maroon;
                txtHighScore.TextAlign = ContentAlignment.MiddleCenter;
            }
        }


    }
}
