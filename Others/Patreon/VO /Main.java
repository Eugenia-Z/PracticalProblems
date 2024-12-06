

import java.util.ArrayList;
import java.util.List;

// Item Class
class Item {
    private String name;
    private double price;
    private int quantity;

    public Item(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public int getQuantity() {
        return quantity;
    }

    public double getTotalPrice() {
        return price * quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
}

// Abstract Coupon Class
abstract class Coupon {
    protected String description;

    public Coupon(String description) {
        this.description = description;
    }

    public abstract double applyDiscount(Item item);

    public String getDescription() {
        return description;
    }
}

// Percentage Discount Coupon
class PercentageDiscountCoupon extends Coupon {
    private double discountPercentage;

    public PercentageDiscountCoupon(String description, double discountPercentage) {
        super(description);
        this.discountPercentage = discountPercentage;
    }

    @Override
    public double applyDiscount(Item item) {
        return item.getTotalPrice() * (discountPercentage / 100);
    }
}

// Bulk Purchase Discount Coupon
class BulkDiscountCoupon extends Coupon {
    private double discountAmount;
    private int minQuantity;

    public BulkDiscountCoupon(String description, double discountAmount, int minQuantity) {
        super(description);
        this.discountAmount = discountAmount;
        this.minQuantity = minQuantity;
    }

    @Override
    public double applyDiscount(Item item) {
        if (item.getQuantity() >= minQuantity) {
            return discountAmount;
        }
        return 0;
    }
}

// Cart Class
class Cart {
    private List<Item> items;
    private List<Coupon> coupons;
    private double totalPrice;
    private double totalDiscount;

    public Cart() {
        items = new ArrayList<>();
        coupons = new ArrayList<>();
        totalPrice = 0;
        totalDiscount = 0;
    }

    public void addItem(Item item) {
        items.add(item);
    }

    public void addCoupon(Coupon coupon) {
        coupons.add(coupon);
    }

    public List<Item> getItems() {
        return items;
    }

    public List<Coupon> getCoupons() {
        return coupons;
    }

    public double calculateTotalPrice() {
        totalPrice = 0;
        for (Item item : items) {
            totalPrice += item.getTotalPrice();
        }
        return totalPrice;
    }

    public double calculateTotalDiscount() {
        totalDiscount = 0;
        for (Item item : items) {
            for (Coupon coupon : coupons) {
                totalDiscount += coupon.applyDiscount(item);
            }
        }
        return totalDiscount;
    }

    public double getFinalPrice() {
        return calculateTotalPrice() - calculateTotalDiscount();
    }

    public void printCartDetails() {
        System.out.println("Cart Details:");
        for (Item item : items) {
            System.out.println("- " + item.getName() + ": $" + item.getPrice() + " x " + item.getQuantity() + " = $"
                    + item.getTotalPrice());
        }
        System.out.println("Total Price: $" + calculateTotalPrice());
        System.out.println("Total Discount: $" + calculateTotalDiscount());
        System.out.println("Final Price: $" + getFinalPrice());
    }
}

// this implementation actually applies all the coupons to all items. 

// Main Class
class Main {
    public static void main(String[] args) {
        // Create Items
        Item apples = new Item("Apples", 2.5, 4); // $2.5 per apple, 4 apples
        Item bananas = new Item("Bananas", 1.0, 10); // $1 per banana, 10 bananas

        // Create Coupons
        Coupon percentageCoupon = new PercentageDiscountCoupon("10% off", 10);
        Coupon bulkCoupon = new BulkDiscountCoupon("$5 off if you buy 2 or more", 5, 2);

        // Create Cart and Add Items and Coupons
        Cart cart = new Cart();
        cart.addItem(apples);
        cart.addItem(bananas);
        cart.addCoupon(percentageCoupon);
        cart.addCoupon(bulkCoupon);

        // Print Cart Details
        cart.printCartDetails();
    }
}
