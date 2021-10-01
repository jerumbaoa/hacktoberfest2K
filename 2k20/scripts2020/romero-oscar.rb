class Invader
  def initialize
    self.animate
  end

  def down
    puts "      ▒▒          ▒▒"
    puts "        ▒▒      ▒▒"
    puts "      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
    puts "    ▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒"
    puts "  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
    puts "  ▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒"
    puts "  ▒▒  ▒▒          ▒▒  ▒▒"
    puts "        ▒▒▒▒  ▒▒▒▒"
  end

  def up
    puts "      ▒▒          ▒▒"
    puts "  ▒▒    ▒▒      ▒▒    ▒▒"
    puts "  ▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒"
    puts "  ▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒"
    puts "  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
    puts "    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
    puts "      ▒▒          ▒▒"
    puts "    ▒▒              ▒▒"
  end

  def animate
    10.times do
      system('clear')
      self.down
      sleep (0.5)
      system('clear')
      self.up
      sleep(0.5)
    end
  end
end

alien = Invader.new
