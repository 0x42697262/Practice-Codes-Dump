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
    <div >
      <h3>{task.title}</h3>
      <p >{task.description}</p>
    </div>
  );
}
