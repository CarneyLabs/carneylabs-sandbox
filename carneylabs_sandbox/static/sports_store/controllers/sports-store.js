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
    .controller("SportsStoreController", SportsStoreController)
    .controller("ProductListController", ProductListController);

//--------------------------------------------------
// Controllers
//--------------------------------------------------

function SportsStoreController($scope,
                               $http,
                               dataUrl)
{
    $scope.data = {};

    $http.get(dataUrl)
        .success(function(data) {
            $scope.data.products = data;
        })
        .error(function(error) {
            $scope.data.error = error;
        });
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