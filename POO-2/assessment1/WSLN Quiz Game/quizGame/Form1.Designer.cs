namespace quizGame
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            pictureBox1 = new PictureBox();
            button1 = new Button();
            button2 = new Button();
            button3 = new Button();
            button4 = new Button();
            lblQuestion = new Label();
            lblLives = new Label();
            lblHint = new Label();
            btnHint = new Button();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
            SuspendLayout();
            // 
            // pictureBox1
            // 
            pictureBox1.BackColor = Color.Yellow;
            pictureBox1.Image = Properties.Resources.questions;
            pictureBox1.Location = new Point(26, 15);
            pictureBox1.Margin = new Padding(4, 3, 4, 3);
            pictureBox1.Name = "pictureBox1";
            pictureBox1.Size = new Size(894, 351);
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
            pictureBox1.TabIndex = 0;
            pictureBox1.TabStop = false;
            // 
            // button1
            // 
            button1.Location = new Point(9, 543);
            button1.Margin = new Padding(4, 3, 4, 3);
            button1.Name = "button1";
            button1.Size = new Size(414, 58);
            button1.TabIndex = 1;
            button1.Tag = "1";
            button1.Text = "button1";
            button1.UseVisualStyleBackColor = true;
            button1.Click += ClickAnswerEvent;
            // 
            // button2
            // 
            button2.Location = new Point(506, 543);
            button2.Margin = new Padding(4, 3, 4, 3);
            button2.Name = "button2";
            button2.Size = new Size(414, 58);
            button2.TabIndex = 1;
            button2.Tag = "2";
            button2.Text = "button1";
            button2.UseVisualStyleBackColor = true;
            button2.Click += ClickAnswerEvent;
            // 
            // button3
            // 
            button3.Location = new Point(9, 640);
            button3.Margin = new Padding(4, 3, 4, 3);
            button3.Name = "button3";
            button3.Size = new Size(414, 58);
            button3.TabIndex = 1;
            button3.Tag = "3";
            button3.Text = "button1";
            button3.UseVisualStyleBackColor = true;
            button3.Click += ClickAnswerEvent;
            // 
            // button4
            // 
            button4.Location = new Point(506, 640);
            button4.Margin = new Padding(4, 3, 4, 3);
            button4.Name = "button4";
            button4.Size = new Size(414, 58);
            button4.TabIndex = 1;
            button4.Tag = "4";
            button4.Text = "button1";
            button4.UseVisualStyleBackColor = true;
            button4.Click += ClickAnswerEvent;
            // 
            // lblQuestion
            // 
            lblQuestion.Font = new Font("Microsoft Sans Serif", 14.25F, FontStyle.Bold, GraphicsUnit.Point, 0);
            lblQuestion.Location = new Point(9, 437);
            lblQuestion.Margin = new Padding(4, 0, 4, 0);
            lblQuestion.Name = "lblQuestion";
            lblQuestion.Size = new Size(925, 85);
            lblQuestion.TabIndex = 2;
            lblQuestion.Text = "Question";
            lblQuestion.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // lblLives
            // 
            lblLives.AutoSize = true;
            lblLives.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            lblLives.Location = new Point(26, 397);
            lblLives.Name = "lblLives";
            lblLives.Size = new Size(56, 21);
            lblLives.TabIndex = 3;
            lblLives.Text = "Lives: ";
            // 
            // lblHint
            // 
            lblHint.AutoSize = true;
            lblHint.Location = new Point(374, 406);
            lblHint.Name = "lblHint";
            lblHint.Size = new Size(38, 15);
            lblHint.TabIndex = 4;
            lblHint.Text = "label1";
            // 
            // btnHint
            // 
            btnHint.Location = new Point(272, 402);
            btnHint.Name = "btnHint";
            btnHint.Size = new Size(75, 23);
            btnHint.TabIndex = 5;
            btnHint.Text = "Show Hint";
            btnHint.UseVisualStyleBackColor = true;
            btnHint.Click += ShowHint;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(933, 704);
            Controls.Add(btnHint);
            Controls.Add(lblHint);
            Controls.Add(lblLives);
            Controls.Add(lblQuestion);
            Controls.Add(button4);
            Controls.Add(button3);
            Controls.Add(button2);
            Controls.Add(button1);
            Controls.Add(pictureBox1);
            Margin = new Padding(4, 3, 4, 3);
            Name = "Form1";
            Text = "Simple Quiz Game MOO ICT";
            ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
            ResumeLayout(false);
            PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Label lblQuestion;
        private Label lblLives;
        private Label lblHint;
        private Button btnHint;
    }
}
