namespace quizGame
{
    internal class QuestionManager
    {

        static Random rng = new Random();
        public void ShuffleQuestions(List<Question> questions) //Question Shuffler
        {
            for (int i = questions.Count - 1; i > 0; i--)
            {
                int j = rng.Next(i + 1);

                var temp = questions[i];
                questions[i] = questions[j];
                questions[j] = temp;
            }
        }

        //------------------------EASY QUESTIONS-----------------------------//-----------------------------//

        public List<Question> EasyQuestions = new()
        {

        new Question
        {
            Text = "Which company created the Mario series?",
            Answers = new string[] { "Nintendo", "Sony", "Microsoft", "Sega" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.mario,
            Hint = "A Japanese company famous for red plumbers and the Switch."
        },

        new Question
        {
            Text = "Which console is made by Sony?",
            Answers = new string[] { "Xbox", "PlayStation", "Switch", "GameCube" },
            CorrectAnswer = 2,
            Picture = Properties.Resources.consoles,
            Hint = "Its latest version is the PS5."
        },

        new Question
        {
            Text = "Which game features the character Steve?",
            Answers = new string[] { "Fortnite", "Minecraft", "Terraria", "Roblox" },
            CorrectAnswer = 2,
            Picture = Properties.Resources.minecraft,
            Hint = "A sandbox game made of blocks."
        },
        new Question
        {
            Text = "Which character is the mascot of Nintendo?",
            Answers = new string[] { "Mario", "Link", "Kirby", "Samus" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.nintendo,
            Hint = "An Italian plumber with a red hat."
        },

        new Question
        {
            Text = "Which game is about building with blocks?",
            Answers = new string[] { "Fortnite", "Minecraft", "Terraria", "Roblox" },
            CorrectAnswer = 2,
            Picture = Properties.Resources.minecraft2,
            Hint = "You can punch trees to start crafting tools."
        },

        new Question
        {
            Text = "Which company created the PlayStation?",
            Answers = new string[] { "Sony", "Microsoft", "Nintendo", "Sega" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.playstation5,
            Hint = "A Japanese electronics giant."
        },

        new Question
        {
            Text = "Which company created the Halo series?",
            Answers = new string[] { "Bungie", "Ubisoft", "Bethesda", "Valve" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.halo,
            Hint = "The same studio later made Destiny."
        },

        new Question
        {
            Text = "Which game features the character Link?",
            Answers = new string[] { "Zelda", "Metroid", "Final Fantasy", "Pokemon" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.link,
            Hint = "A fantasy adventure series involving the Triforce."
        },

        new Question
        {
            Text = "Which company created Fortnite?",
            Answers = new string[] { "Epic Games", "EA", "Ubisoft", "Valve" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.fortnite,
            Hint = "They also created Unreal Engine."
        },

        new Question
        {
            Text = "Which console is made by Microsoft?",
            Answers = new string[] { "PlayStation", "Switch", "Xbox", "GameCube" },
            CorrectAnswer = 3,
            Picture = Properties.Resources.consoles,
            Hint = "Its controller has colored ABXY buttons."
        }
        };

        //------------------------MEDIUM QUESTIONS-----------------------------//-----------------------------//

        public List<Question> MediumQuestions = new()
        {

        new Question
        {
            Text = "Which company developed the game 'The Witcher 3'?",
            Answers = new string[] { "Ubisoft", "Bethesda", "CD Projekt Red", "Bioware" },
            CorrectAnswer = 3,
            Picture = Properties.Resources.gamecomp,
            Hint = "A Polish studio also behind Cyberpunk 2077."
        },

        new Question
        {
            Text = "Which company owns the Xbox brand?",
            Answers = new string[] { "Sony", "Microsoft", "Valve", "Nintendo" },
            CorrectAnswer = 2,
            Picture = Properties.Resources.consoles,
            Hint = "They also created Windows."
        },

        new Question
        {
            Text = "Which engine is commonly used to create indie games?",
            Answers = new string[] { "Frostbite", "Unity", "RAGE", "Snowdrop" },
            CorrectAnswer = 2,
            Picture = Properties.Resources.gameengine,
            Hint = "A very popular engine for small and mobile games."

        },
        new Question
        {
            Text = "Which company developed the Assassin's Creed series?",
            Answers = new string[] { "Ubisoft", "EA", "Valve", "Bethesda" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.ac,
            Hint = "A French publisher known for open-world games."
        },

        new Question
        {
            Text = "Which game studio created Skyrim?",
            Answers = new string[] { "Bethesda", "Bioware", "CD Projekt Red", "Valve" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.gamecomp,
            Hint = "They also made Fallout 3 and Fallout 4."
        },

        new Question
        {
            Text = "Which company developed the FIFA series?",
            Answers = new string[] { "EA Sports", "Konami", "2K", "Ubisoft" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.gamecomp,
            Hint = "Their slogan is 'It's in the game'."
        },

        new Question
        {
            Text = "Which game popularized the battle royale genre in 2017?",
            Answers = new string[] { "PUBG", "Fortnite", "Apex Legends", "Warzone" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.battleroyales,
            Hint = "It was inspired by a mod called PlayerUnknown."
        },

        new Question
        {
            Text = "Which company developed Overwatch?",
            Answers = new string[] { "Blizzard", "Valve", "Riot", "Epic Games" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.overwatch,
            Hint = "Also known for Warcraft and Diablo."
        },

        new Question
        {
            Text = "Which game features the character Kratos?",
            Answers = new string[] { "God of War", "Devil May Cry", "Dark Souls", "Elden Ring" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.soulslike,
            Hint = "A PlayStation series about Greek and Norse gods."
        },

        new Question
        {
            Text = "Which studio created the Grand Theft Auto series?",
            Answers = new string[] { "Rockstar Games", "Ubisoft", "EA", "Valve" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.gta5,
            Hint = "Also known for Red Dead Redemption."
        }
        };

        //------------------------HARD QUESTIONS-----------------------------//-----------------------------//

        public List<Question> HardQuestions = new()
        {

        new Question
        {
            Text = "Which company created the Steam platform?",
            Answers = new string[] { "Epic Games", "Valve", "Ubisoft", "Rockstar" },
            CorrectAnswer = 2,
            Picture = Properties.Resources.steam,
            Hint = "They also created Half-Life and Portal."
        },

        new Question
        {
            Text = "Which studio developed the Dark Souls series?",
            Answers = new string[] { "Capcom", "FromSoftware", "Square Enix", "Konami" },
            CorrectAnswer = 2,
            Picture = Properties.Resources.soulslike,
            Hint = "A Japanese studio famous for extremely difficult games."
        },

        new Question
        {
            Text = "Which company developed the Unreal Engine?",
            Answers = new string[] { "Epic Games", "Valve", "Unity Technologies", "Crytek" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.gameengine,
            Hint = "They also created Fortnite."
        },
        new Question
        {
            Text = "Which company developed the CryEngine?",
            Answers = new string[] { "Crytek", "Valve", "Epic Games", "EA" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.gameengine,
            Hint = "The engine used for the Crysis games."
        },

        new Question
        {
            Text = "Which studio developed Elden Ring?",
            Answers = new string[] { "FromSoftware", "Capcom", "Square Enix", "Konami" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.eldenring,
            Hint = "The same developers behind Dark Souls."
        },

        new Question
        {
            Text = "Which company publishes the Total War series?",
            Answers = new string[] { "SEGA", "EA", "Ubisoft", "Paradox" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.totalwar,
            Hint = "A Japanese company once famous for the Genesis console."
        },

        new Question
        {
            Text = "Which company developed the Source Engine?",
            Answers = new string[] { "Valve", "Epic Games", "Id Software", "Crytek" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.gameengine,
            Hint = "Used in Half-Life 2 and Counter-Strike."
        },

        new Question
        {
            Text = "Which company owns the game studio Bethesda?",
            Answers = new string[] { "Microsoft", "Sony", "EA", "Nintendo" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.gamecomp,
            Hint = "They acquired Bethesda in 2021."
        },

        new Question
        {
            Text = "Which company developed the Doom series originally?",
            Answers = new string[] { "Id Software", "Valve", "Epic Games", "Blizzard" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.doom,
            Hint = "One of the pioneers of FPS games in the 90s."
        },

        new Question
        {
            Text = "Which company developed the REDengine used in Cyberpunk 2077?",
            Answers = new string[] { "CD Projekt Red", "Ubisoft", "EA", "Crytek" },
            CorrectAnswer = 1,
            Picture = Properties.Resources.cyberpunk,
            Hint = "The same company behind The Witcher series."
        }

        };

    }
}
