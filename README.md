## Lab4_OOP

## Features

- **Classes for Different Entities**:
  - `Plant`: Grows passively and reproduces when it gains enough energy.
  - `Herbivore`: Eats plants and reproduces upon reaching an energy threshold.
  - `Carnivore`: Hunts herbivores and omnivores for food.
  - `Omnivore`: Eats both plants and herbivores.
- **Energy Management**:
  - Moving, eating, and reproducing consume energy.
  - Eating food restores energy based on the prey's energy value.
- **Reproduction**: Entities reproduce when their energy exceeds a specified threshold.
- **Entity Notifications**: Events like births, deaths, and eating are printed to the console.
- **Simulation Display**: The grid's state is printed after each simulation step.

## Rules of Interaction

1. **Movement**:
   - Animals move randomly one step per turn.
   - Movement costs 

2. **Eating**:
   - Herbivores and omnivores eat plants within a 3x3 radius.
   - Carnivores eat herbivores and omnivores within a 3x3 radius.
   - Entities gain energy equivalent to the energy of consumed food.

3. **Reproduction**:
   - Plants reproduce at an energy threshold of 20, losing 10 energy in the process.
   - Herbivores reproduce at a threshold of 30, losing 15 energy.
   - Carnivores reproduce at a threshold of 40, losing 20 energy.
   - Omnivores reproduce at a threshold of 35, losing 18 energy.

4. **Death**:
   - Entities die if their energy drops to 0.

## Class Structure

### `EcosystemEntity` (Abstract)
- Base class for all entities (plants and animals).
- Common attributes: `name`, `energy`, `position`, `survival_rate`.
- Abstract method: `act()`.

### Derived Classes
- **`Plant`**: Gains energy passively and reproduces.
- **`Animal`** (Abstract): Includes methods for movement, eating, and reproduction.
  - **`Herbivore`**: Eats plants.
  - **`Carnivore`**: Hunts herbivores and omnivores.
  - **`Omnivore`**: Eats both plants and herbivores.

### `Ecosystem`
- Manages the grid and interactions between entities.
- Functions:
  - `add_entity(entity)`: Adds a new entity.
  - `remove_entity(entity)`: Removes an entity.
  - `get_entities_in_area(position, radius)`: Returns entities within a given radius.
  - `step()`: Simulates one step of the ecosystem.
  - `display()`: Prints the current state of the ecosystem.

