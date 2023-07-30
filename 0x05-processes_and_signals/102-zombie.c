#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * create_zombie_process - Function to create 5 zombie processes
 */

void create_zombie_process(void)
{
pid_t child_pid;
int i;

for (i = 0; i < 5; i++)
{
child_pid = fork();

if (child_pid == 0)
{
exit(0);
}
else if (child_pid > 0)
{
printf("Zombie process created, PID: %d\n", child_pid);
}
else
{
perror("Fork failed");
exit(1);
}
}

for (i = 0; i < 5; i++)
{
wait(NULL);
}
}

/**
 * main - Entry point of the program
 *
 * Return: Always 0
 */
int main(void)
{
create_zombie_process();
return (0);
}
