import { Component, OnInit } from '@angular/core';
import { ExpenseService } from '../expense.service';

@Component({
  selector: 'app-expense',
  templateUrl: './expense.component.html',
  styleUrls: ['./expense.component.css']
})
export class ExpenseComponent implements OnInit {
  expenses: any[] = [];
  newExpense: any = {
    date: '',
    description: '',
    amount: '',
    category: ''
  };
  searchQuery: string = '';

  constructor(private expenseService: ExpenseService) { }

  ngOnInit(): void {
    this.loadExpenses();
  }

  loadExpenses(): void {
    this.expenseService.getExpenses().subscribe(data => {
      this.expenses = data;
    });
  }

  addExpense(): void {
    this.expenseService.addExpense(this.newExpense).subscribe(data => {
      this.expenses.push(data);
      this.newExpense = { date: '', description: '', amount: '', category: '' };
    });
  }

  deleteExpense(id: number): void {
    this.expenseService.deleteExpense(id).subscribe(() => {
      this.expenses = this.expenses.filter(expense => expense.id !== id);
    });
  }

  searchExpenses(): void {
    if (this.searchQuery) {
      this.expenses = this.expenses.filter(expense => 
        expense.description.includes(this.searchQuery) ||
        expense.category.includes(this.searchQuery)
      );
    } else {
      this.loadExpenses();
    }
  }
}
