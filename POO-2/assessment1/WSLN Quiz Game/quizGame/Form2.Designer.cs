namespace quizGame
{
    partial class Form2
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
            label1 = new Label();
            button1 = new Button();
            button2 = new Button();
            button3 = new Button();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(371, 264);
            label1.Name = "label1";
            label1.Size = new Size(117, 15);
            label1.TabIndex = 0;
            label1.Text = "Choose the difficulty";
            // 
            // button1
            // 
            button1.Location = new Point(157, 334);
            button1.Name = "button1";
            button1.Size = new Size(75, 23);
            button1.TabIndex = 1;
            button1.Tag = "1";
            button1.Text = "Easy";
            button1.UseVisualStyleBackColor = true;
            button1.Click += ClickAnswerEvent; //added to link buttons and event in Form2
            // 
            // button2
            // 
            button2.Location = new Point(392, 333);
            button2.Name = "button2";
            button2.Size = new Size(73, 24);
            button2.TabIndex = 2;
            button2.Tag = "2";
            button2.Text = "Medium";
            button2.UseVisualStyleBackColor = true;
            button2.Click += ClickAnswerEvent;
            // 
            // button3
            // 
            button3.Location = new Point(628, 334);
            button3.Name = "button3";
            button3.Size = new Size(75, 23);
            button3.TabIndex = 3;
            button3.Tag = "3";
            button3.Text = "Hard";
            button3.UseVisualStyleBackColor = true;
            button3.Click += ClickAnswerEvent;
            // 
            // Form2
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(933, 704);
            Controls.Add(button3);
            Controls.Add(button2);
            Controls.Add(button1);
            Controls.Add(label1);
            Name = "Form2";
            Text = "Form2";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Button button1;
        private Button button2;
        private Button button3;
    }
}