"use client";
import React, { useState } from "react";
import Column from "./Column";
import NewTaskForm from "./NewTaskForm";
import { Task } from "./TaskCard";

type ColumnType = "Todo" | "Doing" | "Done";

type TaskWithColumn = Task & { column: ColumnType };

export default function Board() {
  const [tasks, setTasks] = useState<TaskWithColumn[]>([
    { id: 1, title: "Setup Project", description: "Scaffold Next.js app", column: "Todo" },
    { id: 2, title: "Build Board UI", description: "Board, Column, TaskCard", column: "Doing" },
    { id: 3, title: "Victory Dance", description: "Celebrate Sprint 1", column: "Done" },
  ]);

  function addTask(title: string, description: string) {
    const newTask: TaskWithColumn = {
      id: tasks.length + 1,
      title,
      description,
      column: "Todo",
    };
    setTasks([...tasks, newTask]);
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-6">Kanban Board</h1>
      <NewTaskForm onAdd={addTask} />

      <div className="flex gap-4">
        <Column name="Todo" tasks={tasks.filter((t) => t.column === "Todo")} />
        <Column name="Doing" tasks={tasks.filter((t) => t.column === "Doing")} />
        <Column name="Done" tasks={tasks.filter((t) => t.column === "Done")} />
      </div>
    </div>
  );
}

