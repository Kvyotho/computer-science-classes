public class Weapon {

    private WeaponType type;
    private WeaponRarity rarity;
    private String name;
    private int level;
    private double damage;
    private double range;
    private int magazine;
    private double ap;
    private double armor_damage;
    private double speed_reduction;

    public Weapon(int typeCode, int typeRarity, String name, int level, double damage, double range, int magazine,
            double ap, double armor_damage, double speed_reduction) {
        this.type = WeaponType.values()[typeCode];
        this.rarity = WeaponRarity.values()[typeRarity];
        this.name = name;
        this.level = level;
        this.damage = damage;
        this.range = range;
        this.magazine = magazine;
        this.ap = ap;
        this.armor_damage = armor_damage;
        this.speed_reduction = speed_reduction;
    }

    public enum WeaponType {
        PISTOL, SHOTGUN, SUBMACHINE, RIFLE, SNIPER, UNKNOWN;
    }

    public enum WeaponRarity {
        COMMON, UNCOMMON, RARE, SUPER_RARE, LEGENDARY, EXOTIC;
    }

    public String getTypeString() {
        return this.type.name();
    }

    public double healthDamage(){
        double sum = damage + ap;
        return sum;
    }

}