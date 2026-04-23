public class Player {
    private String name;
    private int hp;
    private int armor;
    private int level;
    private int experience;
    private int movespeed;
    private int maxhp;
    private int maxarmor;
    private int cash;




    public void heal(int a){
        if (a >= 1){
        hp += a;
    }else{
        throw new IllegalArgumentException();
    }
}

    public void lootExp(int a){
        if (a > 0){ 
        experience += a;
        }else{
            throw new IllegalArgumentException();
        }

        if (experience >= 100) {
            level += 1;
            this.experience = 0; //do while xp > 100 to get xp overflow and multiple level ups
            System.out.println("Level up! You are now level: "+ level);
        }
    }
}
