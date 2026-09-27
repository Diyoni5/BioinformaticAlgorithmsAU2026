# Homework 1

ФИО: Ха Ди Ен
Группа: 402

## Выполненные задачи

- Reverse Complement
- Neighbors
- Frequent Words with Mismatches and Reverse Complements

## Git commands

- `git status` — посмотреть состояние файлов
- `git diff` — посмотреть изменения
- `git add FILE` — подготовить файл к коммиту
- `git commit -m "MESSAGE"` — создать коммит
- `git push` — отправить коммиты на GitHub
- `git log --oneline` — посмотреть историю
- `git branch NAME` — создать ветку
- `git switch NAME` — перейти в другую ветку
- `git switch -c NAME` — создать ветку и перейти в неё
- `git merge BRANCH` — выполнить слияние
- `git revert -m 1 HASH` — отменить merge-коммит
- `git revert HASH` — отменить обычный коммит
- `git log --oneline --graph --all` — показать историю и ветвление
- `git branch -d NAME` — удалить локальную ветку
- `git push origin --delete NAME` — удалить удалённую ветку

## Branching and revert

- Состояние после первого слияния

В HW1 из ветки testing попал файл neighbors.py.

- Состояние после отмены слияния

Команда git revert отменила изменения, внесённые веткой testing, и neighbors.py исчез из HW1.

### Результат повторного слияния
1. Я ожидала, что все файлы из testing перенесутся в HW1.
2. На самом деле: frequent_kmers.py добавился, а neighbors.py — нет.
3. Причина: Git запомнил, что neighbors.py уже был отменён через revert, и не считает его новым при еще одном merge.
4. Файл восстановлен командой git revert <ХЕШ_REVERT_КОММИТА>.
