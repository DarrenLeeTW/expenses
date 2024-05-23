import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ExpenseService {

  private apiUrl = 'http://127.0.0.1:5000/api/expenses';

  constructor(private http: HttpClient) { }

  getExpenses(): Observable<any> {
    return this.http.get(this.apiUrl);
  }

  addExpense(expense: any): Observable<any> {
    return this.http.post(this.apiUrl, expense);
  }

  deleteExpense(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`);
  }
}
