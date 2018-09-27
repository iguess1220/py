class Gun:
    def __init__(self,type,damage):
        self.type = type
        self.damage = damage
        self.bullet_count = 20
    def add_bullet(self,count):
        self.bullet_count += count
    def shoot(self,enemy):
        if self.bullet_count <= 0:
            print("没有子弹了")
        else:
            self.bullet_count -= 1
            enemy.hurt(self)
    def __str__(self):
        return "型号: %s 伤害: %d 子弹数量: %d" %(self.type,self.damage,self.bullet_count)

class player:
    def __init__(self,role):
        self.role = role
        self.hp = 100
        self.gun = None
    def fire(self,enemy):
        if self.gun is None:
            print("没有枪")
        else:
            if self.gun.bullet_count > 0:
                self.gun.shoot(enemy)
            else:
                self.gun.add_bullet(20)
    def hurt(self,enmay_gun):
        self.hp -= enmay_gun.damage
        if self.hp > 0:
            print("%s[%d]" %(self.role,self.hp))
        else:
            print("%s已死亡" %self.role)
    def __str__(self):
        if self.hp > 0:
            if  self.gun is None:
                return "%s[%d],没有枪" %(self.role,self.hp)
            else:
                return "%s[%d],枪: {%s}" %(self.role,self.hp,self.gun)
        else:
            return "%s 已死亡" %self.role

Ak = Gun("Ak47",4)
Ak2 = Gun("Awp",3)
Police = player("警察")
Police.gun = Ak
bandit = player("土匪")
bandit.gun = Ak2
for i in range(30):
    Police.fire(bandit)
    bandit.fire(Police)
    print(Police)
    print(bandit)
