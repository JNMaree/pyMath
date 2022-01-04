class Probe:
    drag = 1    # X velocity step decrease
    grav = 1    # Y velocity step decrease
    def __init__(self, mov=None) -> None:
        self.pos = [0,0]    # Position Vector
        self.trajectory = [self.pos]

        if mov is not None:
            self.x_move = mov[0]
            self.y_move = mov[1]
        else:
            self.x_move = 0     # Axis movement coefficients
            self.y_move = 0

        self.success = False
    
    def __str__(self) -> str:
        sret = '' 
        for i in range(len(self.trajectory) - 1):
            sret += f'{self.trajectory[i]}\n'
        sret += f'> {self.trajectory[i + 1]}'
        return sret

    def step(self):
        self.pos[0] += self.x_move
        self.pos[1] += self.y_move

        self.x_move -= self.drag
        self.y_move -= self.grav

        self.trajectory.append(self.pos)

class Launcher:
    def __init__(self, tstr) -> None:
        # Setup Probe
        self.probe = Probe()

        # Setup Target
        eq = tstr.find('=')
        dt = tstr.find('.', eq)
        xr1 = int (tstr[(eq + 1):dt])
        xr2 = int (tstr[(dt + 2):(tstr.find(',', eq))])

        eq = tstr.find('=', eq + 1)
        dt = tstr.find('.', eq)
        yr1 = int(tstr[(eq + 1):dt])
        yr2 = int(tstr[(dt + 2):])
        print(f'x[{xr1},{xr2}], y[{yr1},{yr2}]')

        self.x_min = xr1
        self.x_max = xr2

        self.y_min = yr2
        self.y_max = yr1

    def is_within_target(self, x_pos, y_pos) -> bool:
        if x_pos > self.x_min and x_pos < self.x_max:
            if y_pos < self.y_min and y_pos > self.y_max:
                return True
            else:
                return False
        else:
            return False

    def launch(self, x_velocity, y_velocity) -> Probe:
        probe = Probe([x_velocity, y_velocity])
        while probe.pos[0] <= self.x_max or probe.pos[1] >= self.y_max:
            # Check if position within target area
            if self.is_within_target(probe.pos[0], probe.pos[1]):
                probe.success = True
                return probe
            else:
                probe.step()
        return probe

    def get_highest_launch(self) -> Probe:
        overshoot = False
        # Set starting velocities
        xv = 1
        yv = 0
        highest_probe = None    # Probe with highest launch angle
        while not overshoot:
            highest_probe = self.launch(xv, yv)
            if highest_probe.success:  # Successful launch
                self.yv += 1
            else:
                second_last_x_pos = highest_probe.trajectory[len(highest_probe.trajectory - 2)][0]
                last_x_pos = highest_probe.trajectory[len(highest_probe.trajectory - 1)][0]
                if (last_x_pos - second_last_x_pos) > (self.x_max - self.x_min):
                    overshoot = True
                else:
                    self.xv += 1
        return highest_probe


def main():
    
    target = ''

    relative_path = 'src/tasks/advent_of_code_21/day17_input.txt'
    with open(relative_path, 'r') as f:
        target = f.readline().strip()
    #print(f'target:{targets}')

    #""" Test Case
    target = 'target area: x=20..30, y=-10..-5'
    # """

    probe_launcher = Launcher(target)
    
    print(probe_launcher.get_highest_launch())

if __name__ == '__main__':
    main()