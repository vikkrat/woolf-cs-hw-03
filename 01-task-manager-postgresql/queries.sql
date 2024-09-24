-- Отримати всі завдання певного користувача
SELECT * FROM tasks WHERE user_id = 1;

-- Вибрати завдання за певним статусом
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');

-- Оновити статус конкретного завдання
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1;

-- Отримати список користувачів, які не мають жодного завдання
SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);

-- Додати нове завдання для конкретного користувача
INSERT INTO tasks (title, description, status_id, user_id) VALUES ('New Task', 'Task Description', 1, 1);

-- Отримати всі завдання, які ще не завершено
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

-- Видалити конкретне завдання
DELETE FROM tasks WHERE id = 1;

-- Знайти користувачів з певною електронною поштою
SELECT * FROM users WHERE email LIKE '%@example.com';

-- Оновити ім'я користувача
UPDATE users SET fullname = 'New Name' WHERE id = 1;

-- Отримати кількість завдань для кожного статусу
SELECT status.name, COUNT(tasks.id) FROM tasks JOIN status ON tasks.status_id = status.id GROUP BY status.name;

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
SELECT tasks.* FROM tasks JOIN users ON tasks.user_id = users.id WHERE users.email LIKE '%@example.com';

-- Отримати список завдань, що не мають опису
SELECT * FROM tasks WHERE description IS NULL;

-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
SELECT users.fullname, tasks.title FROM users JOIN tasks ON users.id = tasks.user_id WHERE tasks.status_id = (SELECT id FROM status WHERE name = 'in progress');

-- Отримати користувачів та кількість їхніх завдань
SELECT users.fullname, COUNT(tasks.id) FROM users LEFT JOIN tasks ON users.id = tasks.user_id GROUP BY users.fullname;
