//--------------------------------------------------
// Modules
//--------------------------------------------------

var customFilters = angular.module("customFilters", [])
    .filter("unique", Unique)
    .filter("range", Range)
    .filter("pageCount", PageCount);

//--------------------------------------------------
// Filters
//--------------------------------------------------

function Unique() {
    return function(data, propertyName) {
        if (angular.isArray(data) && angular.isString(propertyName)) {
            var results = [];
            var keys = {};

            for (var i = 0; i < data.length; i++) {
                var value = data[i][propertyName];

                if (angular.isUndefined(keys[value])) {
                    keys[value] = true;
                    results.push(value);
                }
            }

            return results;
        }
        else {
            return data;
        }
    }
}

function Range($filter) {
    return function(data, page, size) {
        if (angular.isArray(data) && angular.isNumber(page) && angular.isNumber(size)) {
            var startIndex = (page - 1) * size;

            if (data.length < startIndex) {
                return [];
            }
            else {
                return $filter("limitTo")(data.splice(startIndex), size);
            }
        }
        else {
            return data;
        }
    }
}

function PageCount() {
    return function(data, size) {
        if (angular.isArray(data)) {
            var result = [];

            for (var i = 0; i < Math.ceil(data.length / size); i++) {
                result.push(i);
            }

            return result;
        }
        else {
            return data;
        }
    }
}