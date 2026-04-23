using System.Drawing.Text;
using System.Windows.Forms;

namespace quizGame
{
    public partial class Form1 : Form
    {
        // variables list for this quiz game
        static QuestionManager qm = new QuestionManager(); //instancing question manager
        List<Question> currentQuestions;

        Question currentQuestion; //var to keep track of current question
        int questionIndex = 0;
        Form2 menu;

        int score;
        int percentage;
        int totalQuestions;
        int lives;
        int difficulty;
        int hints;


        public Form1(int difficultySelected, Form2 menuForm)
        {

            InitializeComponent();
            menu = menuForm;
            difficulty = difficultySelected;

            if (difficulty == 1)
            {
                currentQuestions = qm.EasyQuestions;
                lives = 7;
                hints = 5;
            }
            else if (difficulty == 2)
            {
                currentQuestions = qm.MediumQuestions;
                lives = 5;
                hints = 3;
            }
            else if (difficulty == 3)
            {
                currentQuestions = qm.HardQuestions;
                lives = 3;
                hints = 1;
            }

            qm.ShuffleQuestions(currentQuestions); //shuffles the questions to a random order
            totalQuestions = currentQuestions.Count;
            AskQuestion();

        }

        private void ClickAnswerEvent(object sender, EventArgs e)
        {

            var senderObject = (Button)sender;
            int buttonTag = Convert.ToInt32(senderObject.Tag);




            if (buttonTag == currentQuestion.CorrectAnswer) //checks for correct answer check
            {
                score++;
                System.Media.SystemSounds.Question.Play();
            }
            else
            {
                lives--;
                lblLives.Text = $"Lives: {lives}";
            }

            questionIndex++;

            if (questionIndex < totalQuestions && lives > 0) //condition to continue or end the game
            {
                AskQuestion();
            }
            else
            {
                EndGame();
            }
        }


        private void EndGame() //ending the game and restart logic
        {
            percentage = (int)Math.Round((double)(100 * score) / totalQuestions);

            MessageBox.Show(
                "Quiz Ended\n" +
                "You answered " + score + " correctly\n" +
                "Score: " + percentage + "%"
            );


            menu.Show();  //shows menu again
            this.Close(); //closes the game window
        }

        private void AskQuestion() //Defines the GUI elements as the correspodents 
        {
            currentQuestion = currentQuestions[questionIndex];

            pictureBox1.Image = currentQuestion.Picture;
            lblQuestion.Text = currentQuestion.Text;
            lblLives.Text = $"Lives: {lives}";
            lblHint.Text = $"Hints Left: {hints}";

            button1.Text = currentQuestion.Answers[0];
            button2.Text = currentQuestion.Answers[1];
            button3.Text = currentQuestion.Answers[2];
            button4.Text = currentQuestion.Answers[3];
            btnHint.Enabled = true;

        }

        //private void label1_Click(object sender, EventArgs e)


        private void ShowHint(object sender, EventArgs e)
        {
            if (hints > 0)
            {
                lblHint.Text = currentQuestion.Hint;
                hints--;
                btnHint.Enabled = false;
            }
            else
            {
                btnHint.Enabled = true;
                MessageBox.Show("No hints left!");
            }
        }
    }
}
