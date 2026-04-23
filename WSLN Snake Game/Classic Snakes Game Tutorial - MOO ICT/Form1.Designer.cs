
namespace Classic_Snakes_Game_Tutorial___MOO_ICT
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            components = new System.ComponentModel.Container();
            startButton = new Button();
            snapButton = new Button();
            picCanvas = new PictureBox();
            txtScore = new Label();
            txtHighScore = new Label();
            gameTimer = new System.Windows.Forms.Timer(components);
            lblBoost = new Label();
            lblEffect = new Label();
            ((System.ComponentModel.ISupportInitialize)picCanvas).BeginInit();
            SuspendLayout();
            // 
            // startButton
            // 
            startButton.BackColor = Color.SkyBlue;
            startButton.Font = new Font("Microsoft Sans Serif", 15.75F, FontStyle.Bold, GraphicsUnit.Point, 0);
            startButton.Location = new Point(694, 14);
            startButton.Margin = new Padding(4, 3, 4, 3);
            startButton.Name = "startButton";
            startButton.Size = new Size(133, 65);
            startButton.TabIndex = 0;
            startButton.Text = "Start";
            startButton.UseVisualStyleBackColor = false;
            startButton.Click += StartGame;
            // 
            // snapButton
            // 
            snapButton.BackColor = Color.PaleGreen;
            snapButton.Font = new Font("Microsoft Sans Serif", 15.75F, FontStyle.Bold, GraphicsUnit.Point, 0);
            snapButton.Location = new Point(694, 85);
            snapButton.Margin = new Padding(4, 3, 4, 3);
            snapButton.Name = "snapButton";
            snapButton.Size = new Size(133, 65);
            snapButton.TabIndex = 0;
            snapButton.Text = "Snap";
            snapButton.UseVisualStyleBackColor = false;
            snapButton.Click += TakeSnapShot;
            // 
            // picCanvas
            // 
            picCanvas.BackColor = Color.Silver;
            picCanvas.Location = new Point(10, 14);
            picCanvas.Margin = new Padding(4, 3, 4, 3);
            picCanvas.Name = "picCanvas";
            picCanvas.Size = new Size(677, 785);
            picCanvas.TabIndex = 1;
            picCanvas.TabStop = false;
            picCanvas.Paint += UpdatePictureBoxGraphics;
            // 
            // txtScore
            // 
            txtScore.AutoSize = true;
            txtScore.Font = new Font("Microsoft Sans Serif", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            txtScore.Location = new Point(694, 182);
            txtScore.Margin = new Padding(4, 0, 4, 0);
            txtScore.Name = "txtScore";
            txtScore.Size = new Size(76, 20);
            txtScore.TabIndex = 2;
            txtScore.Text = "Score: 0";
            // 
            // txtHighScore
            // 
            txtHighScore.AutoSize = true;
            txtHighScore.Font = new Font("Microsoft Sans Serif", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            txtHighScore.Location = new Point(694, 226);
            txtHighScore.Margin = new Padding(4, 0, 4, 0);
            txtHighScore.Name = "txtHighScore";
            txtHighScore.Size = new Size(98, 20);
            txtHighScore.TabIndex = 2;
            txtHighScore.Text = "High Score";
            // 
            // gameTimer
            // 
            gameTimer.Interval = 10;
            gameTimer.Tick += GameTimerEvent;
            // 
            // lblBoost
            // 
            lblBoost.AutoSize = true;
            lblBoost.Location = new Point(694, 271);
            lblBoost.Name = "lblBoost";
            lblBoost.Size = new Size(37, 15);
            lblBoost.TabIndex = 3;
            lblBoost.Text = "Boost";
            // 
            // lblEffect
            // 
            lblEffect.AutoSize = true;
            lblEffect.Location = new Point(694, 315);
            lblEffect.Name = "lblEffect";
            lblEffect.Size = new Size(42, 15);
            lblEffect.TabIndex = 4;
            lblEffect.Text = "Effects";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(873, 837);
            Controls.Add(lblEffect);
            Controls.Add(lblBoost);
            Controls.Add(txtHighScore);
            Controls.Add(txtScore);
            Controls.Add(picCanvas);
            Controls.Add(snapButton);
            Controls.Add(startButton);
            Margin = new Padding(4, 3, 4, 3);
            Name = "Form1";
            Text = "Classic Snakes Game MOO ICT";
            KeyDown += KeyIsDown;
            KeyUp += KeyIsUp;
            ((System.ComponentModel.ISupportInitialize)picCanvas).EndInit();
            ResumeLayout(false);
            PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button startButton;
        private System.Windows.Forms.Button snapButton;
        private System.Windows.Forms.PictureBox picCanvas;
        private System.Windows.Forms.Label txtScore;
        private System.Windows.Forms.Label txtHighScore;
        private System.Windows.Forms.Timer gameTimer;
        private Label lblBoost;
        private Label lblEffect;
    }
}

