
"use client";
import React from "react";
import TaskCard, { Task } from "./TaskCard";

type ColumnProps = {
  name: string;
  tasks: Task[];
};

export default function Column({ name, tasks }: ColumnProps) {
  return (
    <div className="w-1/3 p-4 bg-gray-100 rounded-lg">
      <h2 className="text-lg font-bold mb-4">{name}</h2>
      {tasks.length === 0 ? (
        <p className="text-sm text-gray-500">No tasks</p>
      ) : (
        tasks.map((task) => <TaskCard key={task.id} task={task} />)
      )}
    </div>
  );
}


