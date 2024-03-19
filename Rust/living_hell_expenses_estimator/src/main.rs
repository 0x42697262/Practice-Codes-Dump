struct Employment {
    hours_per_day: usize,
    days_per_month: usize,
}

struct Salary {
    per_hour: usize,
    per_day: usize,
    per_month: usize,
}

struct Costs {
    food: usize,
    rent: usize,
    transportation: usize,
    utilities: usize,
    internet: usize,
    emergency: usize,
}

impl Costs {
    fn daily_total(&self) -> i32 {
        (self.food
            + self.rent
            + self.transportation
            + self.utilities
            + self.internet
            + self.emergency) as i32
    }

    fn monthly_total(&self) -> i32 {
        self.daily_total() * 30
    }
}

fn main() {
    let employment = Employment {
        hours_per_day: 8,
        days_per_month: 22,
    };

    let mut salary = Salary {
        per_hour: 125,
        per_day: 125 * employment.hours_per_day,
        per_month: 125 * employment.hours_per_day * employment.days_per_month,
    };

    let mut costs = Costs {
        food: 300,
        rent: 150,
        transportation: 50,
        utilities: 75,
        internet: 75,
        emergency: 200,
    };

    println!("Hourly Salary: {}", salary.per_hour);
    println!("Daily Salary: {}", salary.per_day);
    println!("Monthly Salary: {}", salary.per_month);
    println!("");
    println!("Food: {}", costs.food);
    println!("Rent: {}", costs.rent);
    println!("Transportation: {}", costs.transportation);
    println!("Utilities: {}", costs.utilities);
    println!("Internet: {}", costs.internet);
    println!("Emergency: {}", costs.emergency);
    println!("-------");
    println!("Daily Expenses: {}", costs.daily_total());
    println!("Monthly Expenses: {}", costs.monthly_total());
    println!(
        "Remaining Money: {}",
        salary.per_month as i32 - costs.monthly_total()
    );
}
