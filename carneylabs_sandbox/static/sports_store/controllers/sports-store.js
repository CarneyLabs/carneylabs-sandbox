//--------------------------------------------------
// Modules
//--------------------------------------------------

var sportsStore = angular.module("sportsStore", ["customFilters", "cart", "ngRoute"])
    .config(function($routeProvider) {
        $routeProvider.when("/checkout", {
            templateUrl: "/static/sports_store/views/checkout-summary.html"
        });
        $routeProvider.when("/products", {
            templateUrl: "/static/sports_store/views/product-list.html"
        });
        $routeProvider.when("/placeorder", {
            templateUrl: "/static/sports_store/views/place-order.html"
        });
        $routeProvider.when("/complete", {
            templateUrl: "/static/sports_store/views/thank-you.html"
        });
        $routeProvider.otherwise({
            templateUrl: "/static/sports_store/views/product-list.html"
        });
    })
    .constant("productListActiveClass", "btn-primary")
    .constant("productListPageCount", 3)
    .constant("dataUrl", "http://carneylabs-sandbox.com:8009/sports-store/products")
    .constant("orderUrl", "http://carneylabs-sandbox.com:8009/sports-store/orders")
    .controller("SportsStoreController", SportsStoreController)
    .controller("ProductListController", ProductListController);

//--------------------------------------------------
// Controllers
//--------------------------------------------------

function SportsStoreController($scope,
                               $http,
                               $location,
                               dataUrl,
                               orderUrl,
                               cart)
{
    $scope.data = {};

    $http.get(dataUrl)
        .success(function(data) {
            $scope.data.products = data;
        })
        .error(function(error) {
            $scope.data.error = error;
        });

    $scope.sendOrder = function(shippingDetails) {
        var order = angular.copy(shippingDetails);
        order.products = cart.getProducts();

        $http.post(orderUrl, order)
            .success(function(data) {
                $scope.data.orderId = data.id;
                cart.getProducts().length = 0;
            })
            .error(function(error) {
                $scope.data.orderError = error;
            })
            .finally(function() {
                $location.path("/complete");
            })
    }
}

function ProductListController($scope,
                               $filter,
                               productListActiveClass,
                               productListPageCount,
                               cart)
{
    var selectedCategory = null;

    $scope.selectedPage = 1;
    $scope.pageSize = productListPageCount;

    $scope.selectCategory = function(newCategory) {
        selectedCategory = newCategory;

        $scope.selectedPage = 1;
    }

    $scope.selectPage = function(newPage) {
        $scope.selectedPage = newPage;
    }

    $scope.categoryFilterFunction = function(product) {
        return selectedCategory == null || product.category == selectedCategory;
    }

    $scope.getCategoryClass = function(category) {
        return selectedCategory == category ? productListActiveClass : "";
    }

    $scope.getPageClass = function(page) {
        return $scope.selectedPage == page ? productListActiveClass : "";
    }

    $scope.addProductToCart = function(product) {
        cart.addProduct(product.id, product.name, product.price);
    }
}

//--------------------------------------------------
// Directives
//--------------------------------------------------