using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace quizGame
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void ClickAnswerEvent(object sender, EventArgs e)
        {
            int difficulty = Convert.ToInt32(((Button)sender).Tag);

            Form1 game = new Form1(difficulty, this);
            game.Show();

            this.Hide();
        }
    }
}
