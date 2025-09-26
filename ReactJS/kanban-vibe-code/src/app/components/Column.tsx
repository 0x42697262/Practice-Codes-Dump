
"use client";
import React from "react";
import TaskCard, { Task } from "./TaskCard";

type ColumnProps = {
  name: string;
  tasks: Task[];
};

export default function Column({ name, tasks }: ColumnProps) {
  return (
    <div >
      <h2>{name}</h2>
      {tasks.length === 0 ? (
        <p>No tasks</p>
      ) : (
        tasks.map((task) => <TaskCard key={task.id} task={task} />)
      )}
    </div>
  );
}


