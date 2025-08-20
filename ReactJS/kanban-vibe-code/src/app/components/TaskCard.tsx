"use client";
import React from "react";

export type Task = {
  id: number;
  title: string;
  description: string;
};

type TaskCardProps = {
  task: Task;
};

export default function TaskCard({ task }: TaskCardProps) {
  return (
    <div className="border rounded-lg p-2 shadow-sm bg-white mb-2">
      <h3 className="font-semibold">{task.title}</h3>
      <p className="text-sm text-gray-600">{task.description}</p>
    </div>
  );
}
